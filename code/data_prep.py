# Roll No: 727823TUAM042

from datetime import datetime
import pandas as pd

print("Roll No: 727823TUAM042")
print("Timestamp:", datetime.now())

data = {
    "temperature": [25, 30, 35, 28, 32, 33, 31],
    "sunlight_hours": [6, 8, 9, 7, 8, 9, 7],
    "panel_age": [2, 3, 4, 2, 5, 3, 4],
    "efficiency": [75, 80, 78, 76, 79, 81, 77]
}

df = pd.DataFrame(data)
df.to_csv("processed_data.csv", index=False)

print("Data preprocessing completed")