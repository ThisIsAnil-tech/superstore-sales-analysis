import pandas as pd

def analyze_categories(df):
    category_analysis = df.groupby('category').agg({
        'sales': 'sum',
        'profit': 'sum',
        'Profit_Margin': 'mean',
        'quantity': 'sum',
        'order_id': 'count'
    }).round(2)
    
    category_analysis.columns = ['Total Sales', 'Total Profit', 'Avg Margin %', 'Total Quantity', 'Order Count']
    return category_analysis.sort_values('Total Sales', ascending=False)

def analyze_subcategories(df):
    subcategory_analysis = df.groupby('subcategory').agg({
        'sales': 'sum',
        'profit': 'sum',
        'Profit_Margin': 'mean'
    }).round(2)
    return subcategory_analysis.sort_values('sales', ascending=False)

def get_most_profitable_category(category_df):
    return category_df['Total Profit'].idxmax()

def get_least_profitable_category(category_df):
    return category_df['Total Profit'].idxmin()