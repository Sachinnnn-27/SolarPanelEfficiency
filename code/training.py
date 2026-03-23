# Roll No: 727823TUAM042

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from datetime import datetime
import os

print("Roll No: 727823TUAM042")
print("Timestamp:", datetime.now())

# ✅ FIX: Set local tracking path (avoids permission error)
mlflow.set_tracking_uri("file:./mlruns")

# Set experiment
mlflow.set_experiment("SolarPanelEfficiency_727823TUAM042")

# Dataset
data = {
    "temperature": [25, 30, 35, 28, 32, 33, 31],
    "sunlight_hours": [6, 8, 9, 7, 8, 9, 7],
    "panel_age": [2, 3, 4, 2, 5, 3, 4],
    "efficiency": [75, 80, 78, 76, 79, 81, 77]
}

df = pd.DataFrame(data)

# Features & target
X = df[["temperature", "sunlight_hours", "panel_age"]]
y = df["efficiency"]

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
pred = model.predict(X)

# Metric
mse = mean_squared_error(y, pred)

# Log with MLflow
mlflow.log_metric("mse", mse)
mlflow.sklearn.log_model(model, "model")

print("MSE:", mse)
print("MLflow run completed")