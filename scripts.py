import pandas as pd
from pathlib import Path

input_dir = Path("data_input")
output_dir = Path("data_output")

output_dir.mkdir(exist_ok=True)

files = input_dir.glob("*.json")

for file_path in files:
    print("woring with: ", file_path.name)

    df = pd.read_json(file_path)

    df["status"] = df["status"].fillna("offline")
    df = df[df["status"] =="active"]

    output_file = output_dir / f"clean {file_path.name}"


    df.to_json(output_file, orient="records", indent=4)
    print("saved in:", output_file)




# df.info()
# df.head()
# print(df)