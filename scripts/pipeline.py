import subprocess
import os

# Get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

forecast_script = os.path.join(
    BASE_DIR,
    "forecasting",
    "forecast.py"
)

print("STEP 1: Running Forecasting Pipeline...")

subprocess.run(["python", forecast_script])

print("STEP 2: Forecast dataset updated")

print("PIPELINE EXECUTED SUCCESSFULLY")