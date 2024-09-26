from flask import Flask, render_template, request, redirect, url_for, session
from repositories import methods
import pandas as pd

app = Flask(__name__)

sales_data = pd.DataFrame({
    "Month": [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ],
    "Notebook": [20, 30, 25, 22, 28, 35, 40, 45, 38, 50, 30, 27],
    "Pen": [43, 35, 40, 30, 45, 42, 50, 55, 48, 60, 43, 39],
    "Coffee Mug": [15, 10, 12, 20, 25, 18, 22, 30, 28, 35, 27, 20],
    "Desk Lamp": [50, 60, 55, 45, 60, 55, 65, 70, 62, 75, 50, 48],
    "Calendar": [25, 20, 30, 15, 22, 18, 25, 30, 28, 35, 27, 22]

})

item_prices = {
    "Notebook": 3.99,
    "Pen": 1.50,
    "Coffee Mug": 9.99,
    "Desk Lamp": 15.75,
    "Calendar": 12.00
}




@app.get('/')
def home():
    yearly_revenue = methods.compute_total_sales_per_month(sales_data, item_prices)
    months = yearly_revenue['Month'].tolist()
    total_revenue = [round(revenue, 2) for revenue in yearly_revenue['Total Revenue per Month']]

    # Quarterly sales
    quarterly_sales = {
        'First Quarter': methods.first_quarter_sales_total(sales_data, item_prices),
        'Second Quarter': methods.second_quarter_sales_total(sales_data, item_prices),
        'Third Quarter': methods.third_quarter_sales_total(sales_data, item_prices),
        'Fourth Quarter': methods.fourth_quarter_sales_total(sales_data, item_prices)
    }
    quarterly_sales_values = list(quarterly_sales.values())


    total_overall_revenue = methods.total_overall_revenue(sales_data, item_prices)
    average_monthly_revenue = methods.average_sales_per_month(sales_data, item_prices)
    total_items_sold = methods.total_items_sold(sales_data)
    

    return render_template('index.html', months=months, total_revenue=total_revenue, quarterly_sales=quarterly_sales_values, total_overall_revenue=total_overall_revenue, average_monthly_revenue=average_monthly_revenue, total_items_sold=total_items_sold)


@app.get('/other-graphs')
def other_graphs():
    yearly_items_sold = methods.total_items_sold_per_month(sales_data)
    months = yearly_items_sold['Month'].tolist()
    total_items_sold = yearly_items_sold['Total Number of Items Sold'].tolist()

    revenue_per_item = methods.revenue_per_item(sales_data, item_prices)
    revenue_per_item = revenue_per_item.to_dict(orient='list')

    number_of_items_sold = methods.items_sold_per_month(sales_data)
    number_of_items_sold = number_of_items_sold.to_dict(orient='list')

    return render_template('other-graphs.html', months=months, total_items_sold=total_items_sold, revenue_per_item=revenue_per_item, number_of_items_sold=number_of_items_sold)

