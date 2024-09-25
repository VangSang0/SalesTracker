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
    print(methods.average_sales_year(sales_data))
    print(methods.average_sales_month(sales_data))
    print(methods.total_sales(sales_data))
    print(methods.compute_items_sold_per_month(sales_data))
    print(methods.compute_total_sales_per_item(sales_data, item_prices))
    return render_template('index.html')


