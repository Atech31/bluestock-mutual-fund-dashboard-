import os
import sqlite3
import pandas as pd

# Automatically change directory to where this script is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

conn = sqlite3.connect("bluestock_mf.db")

csv_table_mapping = {
    "01_fund_master.csv": "dim_fund",
    "02_nav_history.csv": "fact_nav",
    "03_aum_by_fund_house.csv": "fact_aum",
    "04_monthly_sip_inflows.csv": "fact_sip_industry",
    "05_category_inflows.csv": "fact_category_inflows",
    "06_industry_folio_count.csv": "fact_industry_folios",
    "07_scheme_performance.csv": "fact_performance",
    "08_investor_transactions.csv": "fact_transactions",
    "09_portfolio_holdings.csv": "fact_portfolio",
    "10_benchmark_indices.csv": "fact_benchmark",
}

for csv_file, table_name in csv_table_mapping.items():
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"Loaded {len(df)} rows into '{table_name}'")
    else:
        print(f"Warning: {csv_file} not found.")

conn.close()
print("Database ingestion completed successfully!")