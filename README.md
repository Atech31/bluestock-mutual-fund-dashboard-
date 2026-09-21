# 📈 BlueStock Mutual Fund Analytics Platform

![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)

An end-to-end FinTech analytics platform designed to ingest, process, clean, and visualize complex mutual fund market datasets. This platform delivers deep insights into scheme performance, investor transaction trends, risk metrics, and AUM (Assets Under Management) growth across major AMC fund houses.

---

## 📌 Executive Summary

The **BlueStock Mutual Fund Analytics Platform** addresses key challenges in evaluating mutual fund performance, risk exposure, and investor demographic behaviors. By organizing scattered data sources into a structured relational database (SQLite/PostgreSQL), running custom statistical risk-calculation engines, and surfacing key metrics through dynamic Power BI dashboards, this project provides actionable intelligence for fund managers, financial analysts, and retail investors.

---

## 🏗️ Technical Architecture & Pipeline Breakdown
1. **Data Ingestion & Ingestion Engine (`ingest_data.py`)**: Loads 11 core financial CSV datasets into a relational database schema.
2. **Exploratory Data Analysis (`01_eda_and_cleaning.ipynb`)**: Normalizes transaction records, handles missing values, and formats date/currency fields.
3. **Risk & Metric Calculations (`calculate_risk.py`)**: Computes critical financial performance metrics including Sharpe Ratio, Alpha, Beta, Volatility, and CAGR.
4. **Data Modeling & Views (`create_views.py`, `CREATE TABLE fintech_transactions (.pgsql`)**: Constructs optimized analytical database views (`pb_view_aum_trends`, `pb_view_fund_overview`, `pb_fact_risk_metrics`) for BI layer connection.
5. **Business Intelligence Layer (Power BI)**: Interactive `.pbix` reports connecting directly to extracted analytics models.

---

## ✨ Key Features & Dashboard Modules

* **Industry & Fund Overview**: High-level market composition, total industry AUM trends, and fund house concentration metrics.
* **Fund Performance Analysis**: Deep dive into Scheme Returns (1Y, 3Y, 5Y), Benchmark Comparisons (vs. Nifty/Sensex indices), and NAV historical growth.
* **SIP & Inflow Trends**: Granular analysis of monthly Systematic Investment Plan (SIP) inflows and sector-wise distribution.
* **Risk & Volatility Matrix**: Evaluation of fund risk profiles using risk-adjusted return ratios and volatility metrics.
* **Investor Demographics**: Breakdown of retail vs. institutional folio distribution, geographic concentration, and transaction behaviors.

---

## 📂 Repository Structure
---

## 🚀 Getting Started Locally

### Prerequisites
* Python 3.9+
* Power BI Desktop
* SQLite or PostgreSQL

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/Atech31/bluestock-mutual-fund-dashboard-.git](https://github.com/Atech31/bluestock-mutual-fund-dashboard-.git)
   cd bluestock-mutual-fund-dashboard-
