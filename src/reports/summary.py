import pandas as pd

def generate_summary(df, region_df, category_df):
    print("\n" + "="*50)
    print("KEY FINDINGS SUMMARY")
    print("="*50)
    
    best_region = region_df['Total Sales'].idxmax()
    worst_region = region_df['Total Sales'].idxmin()
    print(f"\n📍 Best Performing Region: {best_region}")
    print(f"📍 Worst Performing Region: {worst_region}")
    
    most_profitable_category = category_df['Total Profit'].idxmax()
    least_profitable_category = category_df['Total Profit'].idxmin()
    print(f"\n🏆 Most Profitable Category: {most_profitable_category}")
    print(f"⚠️ Least Profitable Category: {least_profitable_category}")
    
    segment_margin = df.groupby('segment')['Profit_Margin'].mean().sort_values(ascending=False)
    print(f"\n📊 Highest Margin Segment: {segment_margin.index[0]} ({segment_margin.iloc[0]:.2f}%)")
    print(f"📊 Lowest Margin Segment: {segment_margin.index[-1]} ({segment_margin.iloc[-1]:.2f}%)")
    
    best_month = df.groupby('MonthName')['sales'].sum().sort_values(ascending=False)
    print(f"\n📅 Best Month for Sales: {best_month.index[0]}")
    print(f"📅 Worst Month for Sales: {best_month.index[-1]}")