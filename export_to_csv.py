import os
import sqlite3
import pandas as pd

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bluestock_mf.db")
conn = sqlite3.connect(db_path)

views = ['view_fund_overview', 'view_aum_trends', 'fact_risk_metrics']

for view in views:
    df = pd.read_sql_query(f"SELECT * FROM {view}", conn)
    csv_filename = f"pb_{view}.csv"
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), csv_filename)
    df.to_csv(csv_path, index=False)
    print(f"Exported {view} successfully to {csv_filename}")

conn.close()