# Data Engineering and Relational Analytics

This repository contains a comprehensive set of solutions for data processing, relational database management, and analytical reporting. The project demonstrates advanced techniques in SQL querying and Python-based data transformation.

## Project Structure

* **part1.sql**: Advanced SQL implementations focusing on relational data extraction and complex aggregations.
* **part1.py**: Python processing scripts utilizing the Pandas library for end-to-end ETL (Extract, Transform, Load) workflows.

## Technical Implementation

### SQL Analytical Layer
* **Relational Joins:** Implemented multi-table joins to consolidate distributed datasets.
* **Complex Aggregation:** Structured data using `GROUP BY` and `HAVING` for filtered metrics.
* **Window Functions:** Leveraged `PARTITION BY` to perform deep-dive analytics without losing row-level detail.

### Python Data Engineering
* **Data Cleansing:** Automated handling of missing values and rigorous data type enforcement for pipeline stability.
* **Fault-Tolerant Logic:** Integrated robust error handling to manage corrupted files and ingestion failures, ensuring high availability of data.
* **Statistical Reporting:** Engineered dynamic pivot tables to analyze multi-dimensional metrics.
