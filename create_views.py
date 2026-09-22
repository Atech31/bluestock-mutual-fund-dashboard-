import os
import sqlite3

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bluestock_mf.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Master Fund Overview View
cursor.execute("DROP VIEW IF EXISTS view_fund_overview;")
cursor.execute("""
CREATE VIEW view_fund_overview AS
SELECT *
FROM fact_performance;
""")

# 2. Monthly AUM Trend View
cursor.execute("DROP VIEW IF EXISTS view_aum_trends;")
cursor.execute("""
CREATE VIEW view_aum_trends AS
SELECT 
    date,
    fund_house AS amc_name,
    aum_crore AS total_aum
FROM fact_aum;
""")

conn.commit()
print("SQL Views created successfully!")
conn.close()