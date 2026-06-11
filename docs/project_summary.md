# Project Summary #

## Overview ##

This project demonstrates an end-to-end healthcare data engineering and analytics workflow using Python, MySQL, DBeaver, and Power BI.

The objective was to analyse healthcare appointment data, identify attendance patterns, and investigate factors associated with missed appointments.

## Project Workflow ##

1. Loaded the raw healthcare appointments dataset from a CSV file.
2. Explored the dataset using Python and Pandas.
3. Cleaned the data by handling invalid records and creating a waiting time feature.
4. Exported the cleaned dataset to a new CSV file.
5. Imported the cleaned data into a MySQL database using DBeaver.
6. Performed SQL validation and analysis queries to verify data quality and generate insights.
7. Created reusable SQL views for reporting.
8. Built an interactive Power BI dashboard using DAX measures and visualisations.

## Tools and Technologies ##

* Python
* Pandas
* MySQL
* DBeaver
* Power BI
* DAX

## Key Metrics ##

The Power BI dashboard includes:

* Total Appointments
* No Show Rate (%)
* Average Waiting Time (Days)
* Average Patient Age
* Missed Appointments Count

## Key Insights ##

* Approximately 20.19% of appointments were missed.
* Female patients accounted for a larger proportion of appointments than male patients.
* Appointment volumes varied significantly across neighbourhoods.
* The average waiting time was approximately 10 days.

## Project Outputs ##

* Cleaned healthcare dataset
* MySQL database and SQL analysis queries
* SQL views for reporting
* Power BI dashboard
* ETL pipeline documentation

## Conclusion ##

This project demonstrates the complete data workflow from raw data ingestion and cleaning through database storage, SQL analysis, and business intelligence reporting. It showcases practical skills in data engineering, SQL, data validation, and dashboard development.