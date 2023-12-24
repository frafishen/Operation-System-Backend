import datetime

def calculate_growth_rates(sales_data):
    growth_rates = []
    for i in range(1, len(sales_data)):
        previous_month_sales = sales_data[i - 1]['total_sales']
        current_month_sales = sales_data[i]['total_sales']
        growth_rate = ((current_month_sales - previous_month_sales) / previous_month_sales) * 100
        growth_rates.append({
            'month': sales_data[i]['sales_date'].strftime("%Y-%m"),
            'growth_rate': growth_rate
        })
    return growth_rates

def calculate_customer_lifetime_value(customer_data):
    avg_monthly_spend = customer_data['avg_monthly_spend']
    avg_lifespan = customer_data['avg_lifespan']
    clv = avg_monthly_spend * avg_lifespan
    return clv

#moving average method
def calculate_forcasting_data(inventory_data):
    n = len(data)
    window_size = 12

    forecasted_data = []
    for i in range(n - window_size + 1):
        window = data[i:i + window_size]
        average = sum(window) / window_size
        forecasted_data.append(average)

    return forecasted_data


def calculate_average_purchase_time(purchase_dates):
    n = len(purchase_dates)

    total_time = 0
    for i in range(1, n):
        purchase_date_i = purchase_dates[i]['created_at']
        purchase_date_prev = purchase_dates[i - 1]['created_at']

        # 計算時間差
        time_difference = purchase_date_i - purchase_date_prev
        total_time += time_difference.days  # 假設以天為單位

    # 計算平均購買時間
    average_purchase_time = total_time / (n - 1)

    return average_purchase_time

def form_pert_chart_tree(order_data):

    info = {
        "nodes": [
            {
                "no.": 1,
                "name": "B1",
                "quantity": 30,
                "date": "2024-01-10"
            },
            {
                "no.": 2,
                "name": "B2",
                "quantity": 90,
                "date": "2024-01-10"
            },
            {
                "no.": 3,
                "name": "M_2",
                "quantity": 60,
                "date": "2023-12-27"
            },
            {
                "no.": 4,
                "name": "M_3",
                "quantity": 120,
                "date": "2023-12-29"
            },
            {
                "no.": 5,
                "name": "M_4",
                "quantity": 100,
                "date": "2024-01-04"
            },
            {
                "no.": 6,
                "name": "R_3",
                "quantity": 120,
                "date": "2023-12-20"
            },
            {
                "no.": 7,
                "name": "R_4",
                "quantity": 480,
                "date": "2024-12-23"
            },
            {
                "no.": 8,
                "name": "R_6",
                "quantity": 120,
                "date": "2024-12-23"
            },
            {
                "no.": 9,
                "name": "R_7",
                "quantity": 300,
                "date": "2024-12-29"
            }
        ]
    }

    return info