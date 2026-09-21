import os
import sqlite3

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bluestock_mf.db")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Master Fund Overview View (combining performance and risk metrics)
cursor.execute("DROP VIEW IF EXISTS view_fund_overview;")
cursor.execute("""
CREATE VIEW view_fund_overview AS
SELECT 
    p.scheme_name,
    p.fund_house,
    p.category,
    p.return_3yr_pct,
    p.sharpe_ratio,
    p.sortino_ratio,
    r.daily_var_95_pct
FROM fact_performance p
LEFT JOIN dim_fund d ON p.scheme_name = d.scheme_name
LEFT JOIN fact_risk_metrics r ON d.amfi_code = r.amfi_code;
""")

# 2. Monthly AUM Trend View
cursor.execute("DROP VIEW IF EXISTS view_aum_trends;")
cursor.execute("""
CREATE VIEW view_aum_trends AS
SELECT 
    fund_house,
    month_year,
    aum_in_crores
FROM fact_aum;
""")

conn.commit()
print("SQL Views created successfully!")
conn.close()