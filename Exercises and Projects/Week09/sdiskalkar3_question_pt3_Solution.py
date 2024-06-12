#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import pandas as pd

csv_file = sys.argv[1]

data = pd.read_csv(csv_file, skiprows=4, usecols=['Year', 'Anomaly'])

data['Year'] = data['Year'].astype(str)
data['Year'] = pd.to_datetime(data['Year'], format='%Y%m')

plt.figure(figsize=(15, 5))
plt.plot(data['Year'], data['Anomaly'], label='Temperature Anomaly')
plt.title('Global Land and Ocean Temperature Anomalies (1850-2023)')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
dates = data['Year'].dt.to_period('Y').unique().to_timestamp().tolist()
plt.xticks(dates[::12], rotation=45)
plt.axhline(0, color='olive', linestyle='--', label='Baseline (1901-2000 avg temp)')
plt.tight_layout()
plt.legend()
plt.grid(True)
plt.savefig('temperature_anomaly_plot.png', dpi=300)
plt.show()