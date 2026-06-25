import pandas as pd

def analyze_manufactory(df, top_n=10):
    manufactory_analysis = df.groupby('manufactory').agg({
        'sales': 'sum',
        'profit': 'sum',
        'quantity': 'sum'
    }).round(2)
    
    manufactory_analysis.columns = ['Total Sales', 'Total Profit', 'Total Quantity']
    return manufactory_analysis.sort_values('Total Sales', ascending=False).head(top_n)