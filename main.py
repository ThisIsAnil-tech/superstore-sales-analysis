import warnings
warnings.filterwarnings('ignore')

from src.config import CLEANED_CSV_PATH
from src.data_loader.loader import load_data, get_data_info
from src.database.db_connector import load_data_to_db, get_record_count
from src.data_cleaner.cleaner import clean_data
from src.analysis.regional import analyze_regions, get_best_region, get_worst_region
from src.analysis.category import analyze_categories, analyze_subcategories, get_most_profitable_category, get_least_profitable_category
from src.analysis.time_series import analyze_daily_sales, analyze_monthly_sales, analyze_yearly_sales
from src.analysis.customer import analyze_top_customers
from src.analysis.product import analyze_top_products
from src.analysis.manufactory import analyze_manufactory
from src.visualizer.plots import create_visualizations
from src.reports.summary import generate_summary

def main():
    df = load_data()
    get_data_info(df)
    
    load_data_to_db(df)
    print(f"Total records in DB: {get_record_count()}")
    
    df_clean = clean_data(df)
    
    print("\n" + "="*50)
    print("BASIC STATISTICS")
    print("="*50)
    print(f"\nTotal Sales: ${df_clean['sales'].sum():,.2f}")
    print(f"Total Profit: ${df_clean['profit'].sum():,.2f}")
    print(f"Total Quantity Sold: {df_clean['quantity'].sum():,.0f}")
    print(f"Average Profit Margin: {df_clean['Profit_Margin'].mean():.2f}%")
    print(f"Number of Orders: {df_clean['order_id'].nunique():,}")
    print(f"Number of Customers: {df_clean['customer'].nunique():,}")
    print(f"Number of Products: {df_clean['product_name'].nunique():,}")
    
    print("\n" + "="*50)
    print("REGIONAL PERFORMANCE")
    print("="*50)
    region_analysis = analyze_regions(df_clean)
    print(region_analysis)
    
    print("\n" + "="*50)
    print("CATEGORY PERFORMANCE")
    print("="*50)
    category_analysis = analyze_categories(df_clean)
    print(category_analysis)
    
    print("\n" + "="*50)
    print("TOP 10 SUB-CATEGORIES BY SALES")
    print("="*50)
    subcategory_analysis = analyze_subcategories(df_clean)
    print(subcategory_analysis.head(10))
    
    print("\n" + "="*50)
    print("TIME SERIES ANALYSIS")
    print("="*50)
    analyze_daily_sales(df_clean)
    analyze_monthly_sales(df_clean)
    analyze_yearly_sales(df_clean)
    
    print("\n" + "="*50)
    print("TOP 5 CUSTOMERS BY SALES")
    print("="*50)
    top_customers = analyze_top_customers(df_clean)
    print(top_customers)
    
    print("\n" + "="*50)
    print("TOP 5 PRODUCTS BY SALES")
    print("="*50)
    top_products = analyze_top_products(df_clean)
    print(top_products)
    
    print("\n" + "="*50)
    print("MANUFACTORY PERFORMANCE")
    print("="*50)
    manufactory_analysis = analyze_manufactory(df_clean)
    print(manufactory_analysis)
    
    print("\n" + "="*50)
    print("DATA QUALITY CHECKS")
    print("="*50)
    negative_profit = df_clean[df_clean['profit'] < 0]
    print(f"\nOrders with negative profit: {len(negative_profit):,}")
    print(f"Total loss from negative profit orders: ${negative_profit['profit'].sum():,.2f}")
    
    zero_discount = df_clean[df_clean['discount'] == 0]
    avg_margin_zero_discount = zero_discount['Profit_Margin'].mean()
    print(f"\nAverage margin for zero discount orders: {avg_margin_zero_discount:.2f}%")
    
    create_visualizations(df_clean)
    
    generate_summary(df_clean, region_analysis, category_analysis)
    
    df_clean.to_csv(str(CLEANED_CSV_PATH), index=False)
    print("\n✅ Cleaned data exported to 'superstore_cleaned.csv'")
    print("✅ Analysis complete! Ready for Power BI dashboard.")

if __name__ == "__main__":
    main()