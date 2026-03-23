# Roll No: 727823TUAM042

from datetime import datetime
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

print("Roll No: 727823TUAM042")
print("Timestamp:", datetime.now())

df = pd.read_csv("processed_data.csv")

X = df[["temperature", "sunlight_hours", "panel_age"]]
y = df["efficiency"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model training completed")