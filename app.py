import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, jsonify)

import psycopg2
import psycopg2.extras
from utils import (calculate_growth_rates, calculate_customer_lifetime_value, form_pert_chart_tree,
                    calculate_forcasting_data, calculate_average_purchase_time)

app = Flask(__name__)
app.config['DEBUG'] = True

DATABASE_NAME = 'os_db'
USER = 'mis_g1'
PASSWORD = 'mis'
HOST = 'localhost'
PORT = 8080

def get_db_connection():
    conn = psycopg2.connect(database=DATABASE_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
    return conn


@app.errorhandler(500)
def handle_500(error):
    app.logger.error(f"500 error: {error}")  # Log the error
    return jsonify({"status": "failed", "message": "Internal server error"}), 500

#get growth rate
@app.route('/client/<id>/sgr', methods=['GET'])
def get_company_sales(id):
    conn = get_db_connection()
    query = '''SELECT s.sales_date, SUM(p.price * s.sold_quantity) AS total_sales
            FROM sales s
            JOIN product p ON s.product_id = p.product_id
            GROUP BY s.sales_date
            ORDER BY s.sales_date;'''

    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    result = [dict(row) for row in data]
    growth_rates = calculate_growth_rates(result)[-6:]
    result = result[-6:]

    return jsonify({'sales revenue': result, 'growth rates': growth_rates})

@app.route('/client/<id>/clv', methods=['GET'])
def get_customer_lifetime_value(id):
    conn = get_db_connection()
    query = f'SELECT c.clv, c.avg_monthly_spend, c.avg_lifespan ' \
            f'FROM client c ' \
            f'WHERE c.client_id = {id};'

    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute(query)
        data = cursor.fetchall()[0]

    if data[0] == None:
        customer_data = {'avg_monthly_spend': data[1], 'avg_lifespan': data[2]}
        result = calculate_customer_lifetime_value(customer_data)
        query = f'UPDATE client ' \
                f'SET clv = {result} ' \
                f'WHERE client_id = {id};'

        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(query)
    else:
        result = data[0]

    return jsonify({'clv': result})

@app.route('/client/<id>/apt', methods=['GET'])
def get_average_purchase_time(id):
    conn = get_db_connection()
    query = f'SELECT c.created_at ' \
            f'FROM client_order c  ' \
            f'WHERE client_id = {id};'

    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute(query)
        data = cursor.fetchall()

    result = [dict(row) for row in data]
    apt = calculate_average_purchase_time(result)

    return jsonify({'average purchase time': apt})

#Pert Chart
@app.route('/order/<id>/pert_chart', methods=['GET'])
def get_pert_chart(id):
    conn = get_db_connection()
    # query = f''

    # with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
    #     cursor.execute(query)
    #     data = cursor.fetchall()


    order_data = []
    info = form_pert_chart_tree(order_data)

    return jsonify({'chart_info': info})



if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=80)
    app.run(host="0.0.0.0", port=8000)
