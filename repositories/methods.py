import pandas as pd

def compute_total_sales_per_month(sales_data, item_prices):
    months = sales_data['Month']
    sales_data_cleaned = sales_data.drop('Month', axis=1)
    revenue = sales_data_cleaned.multiply(pd.Series(item_prices), axis=1)
    total_revenue = revenue.sum(axis=1)
    total_revenue_df = pd.DataFrame({'Month': months, 'Total Revenue per Month': total_revenue})
    return total_revenue_df

def average_sales_per_month(sales_data, item_prices):
    sales_data_cleaned = sales_data.drop('Month', axis=1)
    sales_data_cleaned = sales_data_cleaned.multiply(pd.Series(item_prices), axis=1)
    average_sales = "{:.2f}".format(sales_data_cleaned.mean(axis=1).mean())
    return average_sales

def total_overall_revenue(data, item_prices):
    data_cleaned = data.drop('Month', axis=1)
    revenue = data_cleaned.multiply(pd.Series(item_prices), axis=1)
    total_revenue = revenue.sum().sum()
    return total_revenue

def total_items_sold(data):
    data_cleaned = data.drop('Month', axis=1)
    total_items_sold = data_cleaned.sum().sum()
    return total_items_sold

def total_items_sold_per_month(data):
    months = data['Month']
    data_df_cleaned = data.drop('Month', axis=1)
    data_total_sales_month = data_df_cleaned.sum(axis=1).astype(int)
    data_total_sales_month_df = pd.DataFrame({'Month': months, 'Total Number of Items Sold': data_total_sales_month})
    return data_total_sales_month_df

def revenue_per_item(sales_data, item_prices):
    month = sales_data['Month']
    sales_data_cleaned = sales_data.drop('Month', axis=1)
    revenue = sales_data_cleaned.multiply(pd.Series(item_prices), axis=1)
    revenue_with_month = pd.concat([month, revenue], axis=1)
    return revenue_with_month

def items_sold_per_month(sales_data):
    month = sales_data['Month']
    sales_data_cleaned = sales_data.drop('Month', axis=1)
    sales_data_cleaned_with_month = pd.concat([month, sales_data_cleaned], axis=1)
    return sales_data_cleaned_with_month

def first_quarter_sales(sales_data, item_prices):
    first_quarter_months = sales_data['Month'][:3]
    first_quarter_sales_data = sales_data[:3]
    first_quarter_sales_data = first_quarter_sales_data.drop('Month', axis=1)
    first_quarter_revenue = first_quarter_sales_data.multiply(pd.Series(item_prices), axis=1)
    first_quarter_revenue = first_quarter_revenue.sum(axis=1)
    first_quarter_revenue_with_month = pd.DataFrame({
        'Month': first_quarter_months,
        'Total Sales': first_quarter_revenue
    })
    return first_quarter_revenue_with_month

def second_quarter_sales(sales_data, item_prices):
    second_quarter_months = sales_data['Month'][3:6]
    second_quarter_sales_data = sales_data[3:6]
    second_quarter_sales_data = second_quarter_sales_data.drop('Month', axis=1)
    second_quarter_revenue = second_quarter_sales_data.multiply(pd.Series(item_prices), axis=1)
    second_quarter_revenue = second_quarter_revenue.sum(axis=1)
    second_quarter_revenue_with_month = pd.DataFrame({
        'Month': second_quarter_months,
        'Total Sales': second_quarter_revenue
    })
    return second_quarter_revenue_with_month

def third_quarter_sales(sales_data, item_prices):
    third_quarter_months = sales_data['Month'][6:9]
    third_quarter_sales_data = sales_data[6:9]
    third_quarter_sales_data = third_quarter_sales_data.drop('Month', axis=1)
    third_quarter_revenue = third_quarter_sales_data.multiply(pd.Series(item_prices), axis=1)
    third_quarter_revenue = third_quarter_revenue.sum(axis=1)
    third_quarter_revenue_with_month = pd.DataFrame({
        'Month': third_quarter_months,
        'Total Sales': third_quarter_revenue
    })
    return third_quarter_revenue_with_month

def fourth_quarter_sales(sales_data, item_prices):
    fourth_quarter_months = sales_data['Month'][9:12]
    fourth_quarter_sales_data = sales_data[9:12]
    fourth_quarter_sales_data = fourth_quarter_sales_data.drop('Month', axis=1)
    fourth_quarter_revenue = fourth_quarter_sales_data.multiply(pd.Series(item_prices), axis=1)
    fourth_quarter_revenue = fourth_quarter_revenue.sum(axis=1)
    fourth_quarter_revenue_with_month = pd.DataFrame({
        'Month': fourth_quarter_months,
        'Total Sales': fourth_quarter_revenue
    })
    return fourth_quarter_revenue_with_month

def first_quarter_sales_total(sales_data, item_prices):
    first_quarter_sales_data = sales_data[:3]
    first_quarter_sales_data = first_quarter_sales_data.drop('Month', axis=1)
    first_quarter_revenue = first_quarter_sales_data.multiply(pd.Series(item_prices), axis=1)
    first_quarter_revenue = first_quarter_revenue.sum(axis=1).sum()
    return first_quarter_revenue

def second_quarter_sales_total(sales_data, item_prices):
    second_quarter_sales_data = sales_data[3:6]
    second_quarter_sales_data = second_quarter_sales_data.drop('Month', axis=1)
    second_quarter_revenue = second_quarter_sales_data.multiply(pd.Series(item_prices), axis=1)
    second_quarter_revenue = second_quarter_revenue.sum(axis=1).sum()
    return second_quarter_revenue

def third_quarter_sales_total(sales_data, item_prices):
    third_quarter_sales_data = sales_data[6:9]
    third_quarter_sales_data = third_quarter_sales_data.drop('Month', axis=1)
    third_quarter_revenue = third_quarter_sales_data.multiply(pd.Series(item_prices), axis=1)
    third_quarter_revenue = third_quarter_revenue.sum(axis=1).sum()
    return third_quarter_revenue

def fourth_quarter_sales_total(sales_data, item_prices):
    fourth_quarter_sales_data = sales_data[9:12]
    fourth_quarter_sales_data = fourth_quarter_sales_data.drop('Month', axis=1)
    fourth_quarter_revenue = fourth_quarter_sales_data.multiply(pd.Series(item_prices), axis=1)
    fourth_quarter_revenue = fourth_quarter_revenue.sum(axis=1).sum()
    return fourth_quarter_revenue



