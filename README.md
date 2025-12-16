## Moroccan Dirham Exchange Rate Monitoring

This project focuses on scraping, transforming, and visualizing the exchange rates of the Moroccan Dirham (MAD) against major foreign currencies. The data is extracted daily from the official Bank Al-Maghrib website.

### 1. Objective

The main goal is to establish a robust and automated **ETL (Extract, Transform, Load) pipeline** to reliably collect, clean, store, and analyze daily exchange rate data.

### 2. Technical Stack

The following technologies are used to build and orchestrate the data pipeline:

* **Extraction & Transformation:** Selenium and Pandas
* **Orchestration:** Apache Airflow (for scheduling and managing the pipeline workflow)
* **Data Storage:** PostgreSQL (hosted on Aiven Cloud for scalability and reliability)
* **Visualization:** Looker Studio (for creating interactive dashboards)

### 3. Project Workflow

This diagram illustrates the flow of data from the source (Bank Al-Maghrib) through the processing stages to the final visualization dashboard.


<img width="1200" alt="Project Workflow Diagram" src="https://github.com/user-attachments/assets/286f2486-2671-4d70-9cac-7113d0d12e0b" />

### 4. Key Results and Analysis

The implemented system provides the following actionable insights:

* **Rate Monitoring:** Daily tracking of buying rates, selling rates, and the calculated average rate.
* **Temporal Analysis:** Detailed time-series analysis to identify trends and detect significant deviations or anomalies.
* **Interactive Dashboard:** A dynamic dashboard, directly connected to the PostgreSQL database, enabling real-time data exploration.

#### Visualization Examples

##### a. Global Comparison of Exchange Rates
<img width="1006" height="1061" alt="Global Comparison of Exchange Rates" src="https://github.com/user-attachments/assets/6781a473-de95-466f-b037-9078cde33fec" />

##### b. Time-Series Analysis of Exchange Rates
<img width="1249" height="897" alt="Time-Series Analysis of Exchange Rates" src="https://github.com/user-attachments/assets/62b61ece-f550-4cdb-9906-4eeb26a7de7a" />


__

*Developed by Yassine DARIF - 2025*
