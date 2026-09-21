import os
import sqlite3
import numpy as np
import pandas as pd

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bluestock_mf.db")
conn = sqlite3.connect(db_path)

# 1. Fetch table columns dynamically to prevent errors
nav_df = pd.read_sql_query("SELECT * FROM fact_nav LIMIT 5;", conn)
columns = nav_df.columns.tolist()

# Find the fund identifier column automatically
id_col = [c for c in columns if 'scheme' in c or 'fund' in c or 'code' in c or 'id' in c][0]
date_col = [c for c in columns if 'date' in c][0]
nav_col = [c for c in columns if 'nav' in c or 'value' in c or 'price' in c][-1]

# 2. Query full data using correct column names
query = f"SELECT {id_col}, {date_col}, {nav_col} FROM fact_nav ORDER BY {id_col}, {date_col};"
nav_df = pd.read_sql_query(query, conn)

nav_df[nav_col] = nav_df[nav_col].astype(float)
nav_df['daily_return'] = nav_df.groupby(id_col)[nav_col].pct_change()

# 3. Calculate Value at Risk (VaR 95%)
var_df = nav_df.groupby(id_col)['daily_return'].agg(
    lambda x: np.percentile(x.dropna(), 5) if len(x.dropna()) > 0 else np.nan
).reset_index()
var_df.columns = [id_col, 'daily_var_95_pct']

print("--- ADVANCED RISK METRICS: VALUE AT RISK (95%) ---")
print(var_df.head(10))


# Save calculated risk metrics to SQLite table
var_df.to_sql('fact_risk_metrics', conn, if_exists='replace', index=False)
print("Saved risk metrics to 'fact_risk_metrics' table successfully!")
conn.close()
