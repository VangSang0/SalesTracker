import pandas as pd

def average_sales_year(data):
    data_df_cleaned = data.drop('Month', axis=1)
    data_mean = data_df_cleaned.mean()
    data_total = int(data_mean.sum())
    return data_total

def average_sales_month(data):
    data_df_cleaned = data.drop('Month', axis=1)
    monthly_mean = data_df_cleaned.mean()
    return monthly_mean.astype(int)

def total_sales(data):
    data_df_cleaned = data.drop('Month', axis=1)
    data_total_sales_month = data_df_cleaned.sum(axis=1)
    return data_total_sales_month.astype(int)

def compute_items_sold_per_month(sales_data):
    sales_data_cleaned = sales_data.drop('Month', axis=1)
    return sales_data_cleaned

def compute_total_sales_per_item(sales_data, item_prices):
    sales_data_cleaned = sales_data.drop('Month', axis=1)
    revenue = sales_data_cleaned.multiply(pd.Series(item_prices), axis=1)

    return revenue

