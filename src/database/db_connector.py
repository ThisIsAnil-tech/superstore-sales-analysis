import sqlite3
import pandas as pd
from src.config import DB_PATH

def create_connection():
    return sqlite3.connect(str(DB_PATH))

def load_data_to_db(df, table_name='superstore_sales'):
    conn = create_connection()
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

def get_record_count(table_name='superstore_sales'):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def execute_query(query):
    conn = create_connection()
    result = pd.read_sql_query(query, conn)
    conn.close()
    return result