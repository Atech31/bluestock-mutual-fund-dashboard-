import os
import sqlite3
import pandas as pd

# Always connect to bluestock_mf.db in the script's exact folder
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bluestock_mf.db")
conn = sqlite3.connect(db_path)

query_top_perf = """
SELECT scheme_name, fund_house, return_3yr_pct, sharpe_ratio, sortino_ratio
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;
"""

print("--- TOP 5 FUNDS BY 3-YEAR RETURN ---")
print(pd.read_sql_query(query_top_perf, conn))

conn.close()