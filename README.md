# 📊 Superstore Sales Analysis

An end-to-end data analysis pipeline for the Superstore retail dataset. This project ingests raw sales data, cleans and transforms it, performs multi-dimensional analysis (regional, category, time-series, customer, product, and manufacturer), persists results to a SQLite database, and generates publication-ready visualizations and summary reports.

---

## 🎯 Project Overview

This project analyzes **9,994 retail transactions** spanning 2019–2022 across the United States to uncover actionable business insights around sales performance, profitability, and operational patterns.

### What It Does

| Stage | Description |
|---|---|
| **Data Ingestion** | Loads raw CSV data and validates schema & completeness |
| **Database Storage** | Persists raw data into a local SQLite database for querying |
| **Data Cleaning** | Handles duplicates, parses dates, engineers time & margin features |
| **Multi-Dimensional Analysis** | Regional, category, sub-category, time-series, customer, product, and manufacturer breakdowns |
| **Visualization** | Generates a 4-panel composite chart (saved as PNG) |
| **Reporting** | Outputs a key findings summary to the console |
| **Export** | Saves the cleaned & enriched dataset as a CSV for downstream tools (e.g., Power BI) |

---

## 🏗️ Project Structure

```
Superstore Analysis/
│
├── main.py                        # Entry point — orchestrates the full pipeline
├── requirements.txt               # Python dependencies
├── report.txt                     # Sample output from a full pipeline run
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── superstore_dataset.csv # Source dataset (9,994 rows × 19 columns)
│   └── processed/
│       ├── superstore_cleaned.csv # Cleaned & feature-engineered output
│       └── superstore.db          # SQLite database with raw data
│
├── src/
│   ├── config.py                  # Centralized paths & directory setup
│   ├── data_loader/
│   │   └── loader.py              # CSV loading and initial data inspection
│   ├── data_cleaner/
│   │   └── cleaner.py             # Date parsing, feature engineering, validation
│   ├── database/
│   │   └── db_connector.py        # SQLite connection, load, query utilities
│   ├── analysis/
│   │   ├── regional.py            # Sales & profit by region
│   │   ├── category.py            # Category & sub-category analysis
│   │   ├── time_series.py         # Daily, monthly, yearly sales trends
│   │   ├── customer.py            # Top customers by sales volume
│   │   ├── product.py             # Top products by sales volume
│   │   └── manufactory.py         # Manufacturer performance rankings
│   ├── visualizer/
│   │   └── plots.py               # Matplotlib/Seaborn composite chart generation
│   └── reports/
│       └── summary.py             # Key findings summary generator
│
├── notebooks/
│   └── exploration.ipynb          # Jupyter notebook for interactive exploration
│
└── outputs/
    ├── figures/
    │   └── superstore_analysis.png  # Generated 4-panel visualization
    └── reports/                     # (Reserved for future report exports)
```

---

## ⚙️ Setup & Installation

### Prerequisites

- **Python 3.8+**
- **pip** (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Superstore-Analysis.git
   cd Superstore-Analysis
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

| Package | Purpose |
|---|---|
| `pandas` | Data manipulation and analysis |
| `numpy` | Numerical computing |
| `matplotlib` | Static chart generation |
| `seaborn` | Statistical data visualization |

> **Note:** SQLite is included in Python's standard library — no additional database setup required.

---

## 🚀 Usage

Run the full analysis pipeline with a single command:

```bash
python main.py
```

### Pipeline Execution Flow

```
Load CSV → Inspect Data → Store in SQLite → Clean & Engineer Features
    ↓
Regional Analysis → Category Analysis → Time-Series Analysis
    ↓
Customer Analysis → Product Analysis → Manufacturer Analysis
    ↓
Data Quality Checks → Generate Visualizations → Print Summary
    ↓
Export cleaned CSV
```

### Outputs

| Output | Location |
|---|---|
| Cleaned dataset | `data/processed/superstore_cleaned.csv` |
| SQLite database | `data/processed/superstore.db` |
| Visualization | `outputs/figures/superstore_analysis.png` |
| Console report | Printed to stdout (also saved in `report.txt`) |

---

## 📈 Analysis Modules

### Regional Performance (`src/analysis/regional.py`)
Aggregates sales, profit, average margin, quantity, and order count by geographic region. Identifies best and worst performing regions.

### Category & Sub-Category (`src/analysis/category.py`)
Breaks down performance by product category (Technology, Furniture, Office Supplies) and drills into the top sub-categories by sales with profit margin analysis.

### Time-Series Analysis (`src/analysis/time_series.py`)
Examines sales patterns across three temporal granularities:
- **Daily** — Range and average daily sales
- **Monthly** — Seasonal trends and monthly ranges
- **Yearly** — Year-over-year growth trajectory

### Customer Analysis (`src/analysis/customer.py`)
Identifies the top N customers by total sales, with profit and order count breakdowns.

### Product Analysis (`src/analysis/product.py`)
Ranks the top N products by total sales, including profit and quantity metrics.

### Manufacturer Analysis (`src/analysis/manufactory.py`)
Evaluates manufacturer (brand) performance by sales, profit, and volume.

---

## 📊 Key Findings

> Results from the analysis of 9,994 transactions across 2019–2022.

| Metric | Value |
|---|---|
| **Total Sales** | $2,297,200.86 |
| **Total Profit** | $286,397.02 |
| **Total Quantity Sold** | 37,873 units |
| **Unique Orders** | 5,009 |
| **Unique Customers** | 793 |
| **Unique Products** | 1,849 |

### Regional Highlights

| Region | Sales | Profit |
|---|---|---|
| 🥇 West | $725,457.82 | $108,418.45 |
| 🥈 East | $678,781.24 | $91,522.78 |
| 🥉 Central | $501,239.89 | $39,706.36 |
| South | $391,721.90 | $46,749.43 |

### Category Performance

| Category | Sales | Profit |
|---|---|---|
| Technology | $836,154.03 | Highest profitability |
| Furniture | $741,999.80 | Lowest profitability |
| Office Supplies | $719,047.03 | Highest order volume (6,026) |

### Other Insights

- 📅 **Best month for sales:** November
- 📅 **Worst month for sales:** February
- 📊 **Highest margin segment:** Home Office (0.14%)
- ⚠️ **Orders with negative profit:** 1,871 (total loss: -$156,131.29)
- 📈 **Year-over-year growth:** Sales grew from $484K (2019) to $733K (2022)

---

## 🔧 Data Pipeline Details

### Data Cleaning (`src/data_cleaner/cleaner.py`)

The cleaning module performs the following transformations:

1. **Date Parsing** — Converts `order_date` and `ship_date` to `datetime` objects
2. **Feature Engineering** — Extracts temporal features:
   - `Year`, `Month`, `Quarter`, `Day`, `DayOfWeek`
   - `MonthName`, `YearMonth` (period)
3. **Profit Margin** — Calculates or maps `Profit_Margin` from existing data
4. **High Value Flag** — Boolean flag for orders above the 75th sales percentile

### Database Layer (`src/database/db_connector.py`)

- Uses Python's built-in `sqlite3` module
- Stores raw data in `superstore_sales` table
- Provides `execute_query()` for ad-hoc SQL analysis

### Visualization (`src/visualizer/plots.py`)

Generates a 2×2 composite chart:
1. **Sales by Region** — Horizontal bar chart
2. **Profit by Category** — Horizontal bar chart
3. **Monthly Sales Trend** — Line chart with markers
4. **Top 10 Sub-categories** — Horizontal bar chart

Output is saved at 300 DPI for print-quality resolution.

---

## 📓 Notebooks

The `notebooks/exploration.ipynb` Jupyter notebook provides an interactive environment for ad-hoc data exploration beyond the automated pipeline.

---