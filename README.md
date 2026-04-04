# Automated Data Curation Pipeline

This repository contains an automated Data Engineering pipeline for batch processing and cleaning JSON logs.

## Features

* **Batch Processing:** Utilizes `pathlib` to automatically discover and process all `.json` files in the `data_input` directory.
* **Automated Directory Management:** Safely creates output directories on the fly without throwing errors.
* **Data Cleansing:** Uses `pandas` to handle missing data (fills `NaN` statuses with 'offline').
* **Data Filtering:** Filters datasets to retain only 'active' records.
* **Standardized Output:** Saves cleaned files into a `data_output` folder with a `clean_` prefix for easy tracking.

## Technologies Used

* **Python 3**
* **Pandas** (Data manipulation and transformation)
* **Pathlib** (Object-oriented filesystem paths)