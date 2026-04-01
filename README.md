# Automated Data Curation & QC Pipeline

##  Project Overview
This repository contains a lightweight, automated ETL (Extract, Transform, Load) pipeline built with Python and Pandas. The script is designed to handle raw, unstructured JSON payloads, perform rigorous Quality Control (QC), cleanse the data, and export a verified dataset ready for downstream analysis or AI model training.

##  Features
- **Data Extraction:** Programmatically parses complex/raw data formats (`.json`).
- **Data Cleansing (QC):** Automatically detects and handles missing or corrupted data points (e.g., replacing `NaN` values with safe fallback defaults) to ensure data integrity.
- **Conditional Filtering:** Utilizes Pandas boolean indexing to filter datasets based on specific operational rules (e.g., isolating active users/servers).
- **Automated Export:** Exports the highly accurate, cleansed data back into structured formats (`.json`, `.csv`, `.xlsx`).

##  Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas

##  How It Works
1. **Extract:** The script reads `raw_data.json` containing simulated raw data with missing keys.
2. **Transform:** - Applies `.fillna()` to safely handle missing statuses without crashing the pipeline.
   - Applies a boolean mask to filter out inactive or erroneous entries.
3. **Load:** The verified output is saved as `clean_data.json` using the `records` orientation for seamless integration with other APIs or databases.

##  Usage
To run the script locally:
1. Clone this repository.
2. Ensure Pandas is installed: `pip install pandas`
3. Run the script:
   ```bash
   python scripts.py