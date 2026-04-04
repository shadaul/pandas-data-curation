import pandas as pd
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="pipeline.log",
    filemode="a"
)


input_dir = Path("data_input")
output_dir = Path("data_output")

output_dir.mkdir(exist_ok=True)

files = input_dir.glob("*.json")
logging.warning("it is warning info")

for file_path in files:
    logging.info(f"working with: {file_path.name} " )

    try:
        df = pd.read_json(file_path)

        df["status"] = df["status"].fillna("offline")
        df = df[df["status"] =="active"]

        output_file = output_dir / f"clean {file_path.name}"


        df.to_json(output_file, orient="records", indent=4)
        logging.info(f"saved in: {output_file}" )

    except Exception as e:
        logging.error(f"this file has error: {file_path}. Details: {e}")




# df.info()
# df.head()
# print(df)