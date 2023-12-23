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