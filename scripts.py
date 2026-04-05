import pandas as pd
from pathlib import Path
import logging
import sqlite3



conn = sqlite3.connect("company_logs.db")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="pipeline.log",
    filemode="a"
)

archive_dir = Path("data_archive")
archive_dir.mkdir(exist_ok=True)

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


        # df.to_json(output_file, orient="records", indent=4)
        df.to_sql("active_logs", conn, if_exists="append", index=False)
        logging.info(f"saved to database table 'active_logs'" )

        target_path = archive_dir / file_path.name
        file_path.rename(target_path)
        logging.info(f"saved to archive {target_path}")

    except Exception as e:
        logging.error(f"this file has error: {file_path}. Details: {e}")


conn.close()

# df.info()
# df.head()
# print(df)