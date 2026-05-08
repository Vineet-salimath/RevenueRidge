import pandas as pd

# Load TRAIN dataset directly
df = pd.read_csv(r"D:\RevenueRidge\data\raw\train.csv")
    

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# Sort values
df = df.sort_values("Date")

# Create Moving Average Forecast
df["MA_4"] = df["Weekly_Sales"].rolling(window=4).mean()

# Save forecast dataset
df.to_csv(r"D:\RevenueRidge\data\cleaned\forecast_data.csv", index=False)

print("Forecast dataset created successfully")