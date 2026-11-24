
# Healthcare Appointment Analysis Pipeline

## Project Overview

This project demonstrates an end-to-end healthcare data engineering and analytics pipeline using Python, Pandas, MySQL, SQL, Power BI, and AWS cloud services for data storage and analytical processing.

The aim of the project is to process and analyse healthcare appointment data through data extraction, cleaning, transformation, and SQL analysis. It identifies attendance patterns, appointment no-show behaviour, and waiting times. The resulting insights support data-driven decision-making through reporting and visualisation.

---

## Project Architecture

The project follows the workflow below:

<img src="docs/etl_pipeline.png" alt="Project Architecture" width="400">

---

## Technologies Used

* Python
* Pandas
* MySQL
* DBeaver
* Amazon S3
* AWS Glue
* Amazon Athena
* Amazon Aurora (planned)
* Amazon Redshift (planned)
* Power BI
* DAX
* Git
* GitHub

---

## Repository Contents

| Folder | Description |
|---------|-------------|
| data | Raw and cleaned healthcare datasets |
| scripts | Python scripts for data exploration and cleaning |
| sql | Database schema, validation queries, and views |
| dashboards_PowerBI | Power BI dashboard files and screenshots |
| docs | ETL diagram and project documentation |
| screenshots | AWS and Athena query evidence |

---

## Data Cleaning

The dataset was cleaned using Python and Pandas.

Cleaning steps included:

* Converting date columns to the correct format
* Creating a DaysWaiting feature
* Removing invalid age values
* Removing negative waiting times
* Removing duplicate appointment records
* Exporting a cleaned dataset for database loading
* Validating the cleaned dataset

---

## SQL Analysis

SQL was used to:

* Validate row counts
* Check waiting time ranges
* Analyse attendance behaviour
* Explore appointment distributions
* Calculate average waiting times by appointment outcome
* Analyse appointment outcomes by gender
* Identify the top 10 neighbourhoods by appointment volume
* Create reusable reporting views

Example query:

```sql
SELECT COUNT(*)
FROM appointments;
```

---
## AWS Cloud Integration ##

This project explores the use of AWS cloud services to support
healthcare data storage, relational database management and
analytical data warehousing.

AWS services:

* Amazon S3: Cloud storage for healthcare datasets.
* Amazon Aurora: Relational database management.
* Amazon Redshift: Analytical data warehousing.

The AWS architecture supports the preparation and organisation
of healthcare data for downstream reporting and analytics.
---

## AWS Cloud Integration

AWS services were incorporated to support cloud storage, data cataloguing, and analytical processing.

* **Amazon S3:** Stores raw and processed healthcare datasets.
* **AWS Glue:** Crawls datasets and maintains metadata in the Glue Data Catalog.
* **Amazon Athena:** Enables SQL querying of datasets stored in Amazon S3.
* **Amazon Aurora:** Included in the wider architecture as a relational database service.
* **Amazon Redshift:** Included in the wider architecture as an analytical data warehouse.

Amazon S3, AWS Glue and Amazon Athena were used in the implemented cloud workflow. Amazon Aurora and Amazon Redshift are included in the architecture but have not yet been deployed.

---

## Power BI Dashboard

The Power BI dashboard includes:

### KPI Metrics

* Total Appointments
* No Show Rate (%)
* Average Waiting Time (Days)
* Average Patient Age
* Missed Appointments

### Visualisations

* Attended vs Missed Appointments
* Appointments by Gender
* Top 10 Neighbourhoods by Appointments

---

## Dashboard Preview

![Dashboard](dashboards_PowerBI/dashboard_overview.png)

---

## DAX Measures

The Power BI dashboard uses custom DAX measures to calculate key business metrics.

### Total Appointments

```dax
Total Appointments = COUNTROWS(appointments_dashboard)
```

### Average Age

```dax
Average Age = AVERAGE(appointments_dashboard[Age])
```

### Average Waiting Time

```dax
Average Waiting Time = AVERAGE(appointments_dashboard[DaysWaiting])
```

### No Show Count

```dax
No Show Count =
CALCULATE(
    COUNTROWS(appointments_dashboard),
    appointments_dashboard[No-show] = "Yes"
)
```

### No Show Rate %

```dax
No Show Rate % =
DIVIDE(
    [No Show Count],
    [Total Appointments]
)
```

---

## Key Findings

* 20.19% of appointments resulted in a no-show.
* Female patients accounted for the majority of appointments.
* Average waiting time was approximately 10 days.
* Appointment demand varied significantly between neighbourhoods.

---

## Future Improvements

- Implement automated AWS-based data ingestion.
- Introduce pipeline monitoring and error handling.
- Implement automated data quality checks.
- Automate database loading using Python and MySQL Connector.
- Add additional Power BI visuals and drill-through functionality.
- Build a scheduled ETL pipeline.
- Deploy dashboards using Power BI Service.
- Extend cloud integration by deploying Amazon Aurora and Amazon Redshift.

---

### Author

Omoefe Alicia Osayi
