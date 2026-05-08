RevenueRidge: Retail Intelligence System
Overview

RevenueRidge is a retail analytics project designed to transform raw sales data into actionable business insights. It enables analysis of sales performance, store-level trends, and the impact of external factors such as holidays, fuel prices, temperature, and unemployment.

The system integrates data preprocessing, SQL-based analytics, and interactive dashboards to support data-driven decision-making in retail operations.

Objective

The primary objective of this project is to build an end-to-end retail intelligence system that:

Analyzes historical retail sales data
Identifies trends across stores and departments
Evaluates the impact of external economic and seasonal factors
Provides visual insights through dashboards for business decision-making
Tech Stack
Python (Pandas, NumPy)
SQL (PostgreSQL)
Power BI
Jupyter Notebook
VS Code
Project Structure
RevenueRidge/
│
├── data/
│   ├── raw/                 # Original datasets
│   └── cleaned/             # Processed datasets
│
├── notebooks/
│   ├── phase1_cleaning.ipynb
│   ├── phase2_eda.ipynb
│
├── sql/
│   └── queries.sql          # SQL analysis queries
│
├── powerbi/
│   └── dashboard.pbix       # Power BI dashboard
│
├── scripts/
│   └── preprocessing.py
│
└── README.md
Features
Data cleaning and preprocessing pipeline
Exploratory Data Analysis (EDA)
SQL-based business intelligence queries
KPI analysis for sales and revenue trends
Power BI dashboard for interactive visualization
Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/RevenueRidge.git
cd RevenueRidge
2. Install Dependencies
pip install pandas numpy matplotlib seaborn psycopg2
3. Run Notebooks

Launch Jupyter Notebook and execute:

phase1_cleaning.ipynb
phase2_eda.ipynb
Dashboard

Open the Power BI file located in:

powerbi/dashboard.pbix
Key Outcomes
Identification of top-performing stores
Analysis of seasonal and holiday sales patterns
Understanding of external factors affecting revenue
Creation of a structured retail analytics pipeline
Author

Vineet v Salimath
Intern Project: Retail Intelligence System
