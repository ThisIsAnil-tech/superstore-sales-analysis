import pandas as pd

def analyze_daily_sales(df):
    daily_sales = df.groupby('order_date')['sales'].sum()
    print(f"\nDaily Sales Range: ${daily_sales.min():,.2f} to ${daily_sales.max():,.2f}")
    print(f"Average Daily Sales: ${daily_sales.mean():,.2f}")
    return daily_sales

def analyze_monthly_sales(df):
    monthly_sales = df.groupby('YearMonth')['sales'].sum()
    print(f"\nMonthly Sales Range: ${monthly_sales.min():,.2f} to ${monthly_sales.max():,.2f}")
    print(f"Average Monthly Sales: ${monthly_sales.mean():,.2f}")
    return monthly_sales

def analyze_yearly_sales(df):
    yearly_sales = df.groupby('Year')['sales'].sum()
    print(f"\nYearly Sales:")
    print(yearly_sales)
    return yearly_sales

def get_best_month(df):
    best_month = df.groupby('MonthName')['sales'].sum().sort_values(ascending=False)
    return best_month.index[0]

def get_worst_month(df):
    worst_month = df.groupby('MonthName')['sales'].sum().sort_values(ascending=False)
    return worst_month.index[-1]