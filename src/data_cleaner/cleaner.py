import pandas as pd
import numpy as np

def clean_data(df):
    df_clean = df.copy()
    
    df_clean['order_date'] = pd.to_datetime(df_clean['order_date'])
    df_clean['ship_date'] = pd.to_datetime(df_clean['ship_date'])
    
    df_clean['Year'] = df_clean['order_date'].dt.year
    df_clean['Month'] = df_clean['order_date'].dt.month
    df_clean['Quarter'] = df_clean['order_date'].dt.quarter
    df_clean['Day'] = df_clean['order_date'].dt.day
    df_clean['DayOfWeek'] = df_clean['order_date'].dt.dayofweek
    df_clean['MonthName'] = df_clean['order_date'].dt.strftime('%B')
    df_clean['YearMonth'] = df_clean['order_date'].dt.to_period('M')
    
    if 'profit_margin' in df_clean.columns:
        df_clean['Profit_Margin'] = df_clean['profit_margin']
    else:
        df_clean['Profit_Margin'] = (df_clean['profit'] / df_clean['sales']) * 100
    
    df_clean['High_Value'] = df_clean['sales'] > df_clean['sales'].quantile(0.75)
    
    print("\nData Types:")
    print(df_clean.dtypes)
    print("\nMissing values after cleaning:")
    print(df_clean.isnull().sum())
    print("\nDataset Shape:", df_clean.shape)
    
    return df_clean