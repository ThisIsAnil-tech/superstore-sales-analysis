import matplotlib.pyplot as plt
import seaborn as sns
from src.config import FIGURES_DIR

def create_visualizations(df):
    plt.style.use('seaborn-v0_8-darkgrid')
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    region_sales = df.groupby('region')['sales'].sum().sort_values()
    axes[0,0].barh(region_sales.index, region_sales.values, color='skyblue')
    axes[0,0].set_title('Sales by Region')
    axes[0,0].set_xlabel('Total Sales ($)')
    
    category_profit = df.groupby('category')['profit'].sum().sort_values()
    axes[0,1].barh(category_profit.index, category_profit.values, color='lightcoral')
    axes[0,1].set_title('Profit by Category')
    axes[0,1].set_xlabel('Total Profit ($)')
    
    monthly_trend = df.groupby('YearMonth')['sales'].sum().reset_index()
    monthly_trend['YearMonth'] = monthly_trend['YearMonth'].astype(str)
    axes[1,0].plot(monthly_trend['YearMonth'][::3], monthly_trend['sales'][::3], marker='o', color='green')
    axes[1,0].set_title('Monthly Sales Trend')
    axes[1,0].set_xlabel('Month')
    axes[1,0].set_ylabel('Sales ($)')
    axes[1,0].tick_params(axis='x', rotation=45)
    
    top_sub = df.groupby('subcategory')['sales'].sum().sort_values(ascending=False).head(10)
    axes[1,1].barh(top_sub.index, top_sub.values, color='orange')
    axes[1,1].set_title('Top 10 Sub-categories by Sales')
    axes[1,1].set_xlabel('Total Sales ($)')
    
    plt.tight_layout()
    plt.savefig(str(FIGURES_DIR / 'superstore_analysis.png'), dpi=300, bbox_inches='tight')
    plt.show()