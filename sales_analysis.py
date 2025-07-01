# Sales Data Analysis using Pandas

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv') 

print("Data Preview:")
print(df.head())

grouped_data = df.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:")
print(grouped_data)


plt.figure(figsize=(10, 6))
grouped_data.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

