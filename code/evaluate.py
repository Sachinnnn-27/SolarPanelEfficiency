# Roll No: 727823TUAM042

from datetime import datetime
import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error

print("Roll No: 727823TUAM042")
print("Timestamp:", datetime.now())

df = pd.read_csv("processed_data.csv")
model = joblib.load("model.pkl")

pred = model.predict(df[["temperature", "sunlight_hours", "panel_age"]])
mse = mean_squared_error(df["efficiency"], pred)

print("MSE:", mse)
print("Evaluation completed")