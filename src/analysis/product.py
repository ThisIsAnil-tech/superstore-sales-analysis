import pandas as pd

def analyze_top_products(df, top_n=5):
    top_products = df.groupby('product_name').agg({
        'sales': 'sum',
        'profit': 'sum',
        'quantity': 'sum'
    }).round(2)
    
    top_products.columns = ['Total Sales', 'Total Profit', 'Total Quantity']
    return top_products.sort_values('Total Sales', ascending=False).head(top_n)