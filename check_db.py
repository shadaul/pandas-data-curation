import pandas as pd
import sqlite3

conn = sqlite3.connect("company_logs.db")

# query = "SELECT COUNT(*) AS total_active_users FROM active_logs"
query = "SELECT * FROM users"
df = pd.read_sql(query, conn)
print(df)
conn.close()