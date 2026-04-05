# Automated Data Curation & ETL Pipeline

This repository contains a robust Data Engineering pipeline for batch processing, cleaning, and loading JSON logs into a relational database.

## Architecture & Features

* **ETL Process:** Extracts raw JSON logs, transforms them using Pandas, and loads the clean data into an SQLite database (`company_logs.db`).
* **Cold Storage (Idempotency):** Successfully processed files are automatically moved from `data_input` to `data_archive` to prevent duplicate processing on subsequent runs.
* **Fault Tolerance:** Implements strict `try-except` blocks. If a corrupted file is encountered, the script logs the error and continues processing the rest of the batch without crashing.
* **System Logging:** Uses Python's built-in `logging` module to maintain a persistent audit trail (`pipeline.log`) tracking system operations, warnings, and error details.
* **Data Cleansing:** Handles missing data (fills `NaN` statuses with 'offline') and filters datasets to retain only 'active' records.

## Technologies Used

* **Python 3**
* **Pandas** (Data transformation)
* **SQLite3** (Relational database management)
* **Pathlib** (Object-oriented filesystem paths)
* **Logging** (System audit and error tracking)