import pandas as pd


df = pd.read_json("raw_data.json")

df["status"] = df["status"].fillna("offline")
df = df[df["status"] =="active"]

df.to_json("clean_data.json", orient="records", indent=4)

# df.info()
# df.head()
# print(df)