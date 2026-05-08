from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:postgre@localhost:5432/RevenueRidge"
)

conn = engine.connect()
print("✅ Connected successfully")
conn.close()