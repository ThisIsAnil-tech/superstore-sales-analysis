import pandas as pd

def analyze_regions(df):
    region_analysis = df.groupby('region').agg({
        'sales': 'sum',
        'profit': 'sum',
        'Profit_Margin': 'mean',
        'quantity': 'sum',
        'order_id': 'count'
    }).round(2)
    
    region_analysis.columns = ['Total Sales', 'Total Profit', 'Avg Margin %', 'Total Quantity', 'Order Count']
    return region_analysis.sort_values('Total Sales', ascending=False)

def get_best_region(region_df):
    return region_df['Total Sales'].idxmax()

def get_worst_region(region_df):
    return region_df['Total Sales'].idxmin()