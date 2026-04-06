# Automated Data Curation & ETL Pipeline

This repository contains a robust Data Engineering pipeline for batch processing, flattening nested JSON logs from a REST API, and loading them into a relational database.

## Architecture & Features

* **Orchestration:** Utilizes a master script (`main.py`) with the `subprocess` module to manage the execution flow of the entire ETL process.
* **Data Extraction (API):** Automatically fetches raw user data from an external REST API using the `requests` library and lands it into a local Landing Zone (`data_input`).
* **Data Transformation:** Leverages `pandas` to flatten nested JSON structures (e.g., extracting cities from nested address dictionaries) and performs strict column projection to remove unnecessary data.
* **Database Loading:** Safely ingests the cleaned, flat datasets into an SQLite relational database (`users` table) for downstream analytics.
* **Cold Storage (Idempotency):** Successfully processed files are automatically moved to a `data_archive` directory to prevent duplicate processing on subsequent runs.
* **Fault Tolerance & Logging:** Implements strict `try-except` blocks. If a corrupted file or schema drift is encountered, the script logs the error details to `pipeline.log` and continues processing the rest of the batch without crashing.

## Technologies Used

* **Python 3**
* **Pandas** (Data transformation & flattening)
* **Requests** (REST API integration)
* **SQLite3** (Relational database management)
* **Subprocess & Pathlib** (Pipeline orchestration & filesystem management)
* **Logging** (System audit and error tracking)