import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/huanglihan/Desktop/CEE_272R_spring_2024/data_2023_hourly.csv')
print(df)
df['Date & Time'] = pd.to_datetime(df['Date & Time'])
df_Feb = df[df['Date & Time'].dt.month == 2]
# ploting
plt.plot(df_february['Date & Time'], df_february['Usage [kW]'], label='Power [kW]')
plt.title('Electricity Usage in February')
plt.xlabel('Time')
plt.ylabel('Power [kW]')
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('february_power_usage.png')


plt.show()
