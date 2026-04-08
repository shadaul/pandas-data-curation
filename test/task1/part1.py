import pandas as pd

df['total_revenue'] =df['price'] * df['quantity']
avg_revenue = df['total_revenue'].mean()
print(avg_revenue)