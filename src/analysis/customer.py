import pandas as pd

def analyze_top_customers(df, top_n=5):
    top_customers = df.groupby('customer').agg({
        'sales': 'sum',
        'profit': 'sum',
        'order_id': 'count'
    }).round(2)
    
    top_customers.columns = ['Total Sales', 'Total Profit', 'Order Count']
    return top_customers.sort_values('Total Sales', ascending=False).head(top_n)