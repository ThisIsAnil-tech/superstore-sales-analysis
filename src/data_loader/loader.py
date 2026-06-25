import pandas as pd
from src.config import RAW_CSV_PATH

def load_data():
    return pd.read_csv(str(RAW_CSV_PATH))

def get_data_info(df):
    print("Dataset Shape:", df.shape)
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nColumn Info:")
    print(df.info())
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nBasic Statistics:")
    print(df.describe())
    print(f"\nDuplicate rows: {df.duplicated().sum()}")
    return df