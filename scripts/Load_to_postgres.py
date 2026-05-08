import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(
    "data/cleaned/final_retail_data.csv"
)

engine = create_engine(
    "postgresql://postgres:postgre@localhost:5432/RevenueRidge"
)

df.to_sql(
    "retail_sales",
    engine,
    if_exists="replace",
    index=False
)

print("✅ 20k dataset uploaded")