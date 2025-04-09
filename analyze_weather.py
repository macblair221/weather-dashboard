import os
import json
import pandas as pd
import matplotlib.pyplot as plt

data_dir = "weather_data"

files = sorted(os.listdir(data_dir), reverse=True)

latest_file = os.path.join(data_dir, files[0])

with open(latest_file, "r") as f:
    data = json.load(f)

hourly = data['hourly']
df = pd.DataFrame({
	"Time": pd.to_datetime(hourly['time']),
	"Temperature": hourly['temperature_2m'],
	"Humidity": hourly['relative_humidity_2m']
})


plt.figure(figsize=(10, 5)) 

plt.plot(df["Time"], df["Temperature"], label="Temperature (°C)", color="orange")
plt.plot(df["Time"], df["Humidity"], label="Humidity (%)", color="blue")

plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Hourly Temperature and Humidity in Eugene")
plt.legend()
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

