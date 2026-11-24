# Healthcare Appointment Analysis Pipeline

## Project Summary

### 1. Project Objective

The aim of this project was to build an end-to-end healthcare data engineering and analytics pipeline to clean, transform and analyse healthcare appointment data.

The project focuses on identifying appointment attendance patterns, no-show behaviour and waiting times through data processing, SQL analysis, cloud services and interactive data visualisation.

### 2. Dataset

The project uses a healthcare appointment dataset containing information about:

* Patient demographics
* Appointment dates
* Medical conditions
* Patient neighbourhoods
* Appointment attendance outcomes

### 3. Data Engineering and ETL

Python and Pandas were used to perform data exploration, cleaning and transformation.

The ETL process included:

* Extracting the raw healthcare appointment dataset.
* Exploring dataset structure, columns and missing values.
* Converting date columns into the correct datetime format.
* Creating a DaysWaiting feature to calculate appointment waiting times.
* Removing invalid age values.
* Removing records with negative waiting times.
* Exporting the cleaned dataset for further analysis.

### 4. SQL Analysis

SQL and MySQL were used to validate and analyse the cleaned healthcare dataset.

The analysis included:

* Validating total record counts.
* Identifying unique patients.
* Checking minimum and maximum waiting times.
* Calculating average patient age.
* Analysing attended versus missed appointments.
* Exploring appointment distributions by gender.
* Identifying the top 10 neighbourhoods by appointment volume.
* Calculating average waiting times by appointment outcome.

Reusable SQL views were also created to support reporting and analysis.

### 5. AWS Cloud Integration

AWS services were incorporated into the project architecture to support cloud storage, data cataloguing and analytical processing.

The architecture includes:

* Amazon S3: Cloud storage for raw and processed healthcare datasets.
* AWS Glue: Data cataloguing and metadata discovery.
* Amazon Athena: Serverless SQL querying and analytical processing of datasets stored in Amazon S3.
* Amazon Aurora: Relational database management.
* Amazon Redshift: Analytical data warehousing.

Amazon S3, AWS Glue and Amazon Athena were used in the implemented cloud workflow. Amazon Aurora and Amazon Redshift are included in the wider project architecture but have not yet been deployed.

### 6. Power BI Dashboard

Power BI was used to create an interactive dashboard to present the results of the healthcare appointment analysis.

Key Performance Indicators (KPIs):

* Total Appointments
* No-show Rate (%)
* Average Waiting Time (Days)
* Average Patient Age
* Missed Appointments

Dashboard Visualisations:

* Attended vs Missed Appointments
* Appointments by Gender
* Top 10 Neighbourhoods by Appointments

Custom DAX measures were created to calculate the dashboard’s key metrics.

### 7. Key Findings

The analysis identified the following findings:

* 20.19% of appointments resulted in a no-show.
* Female patients accounted for the majority of appointments.
* Average waiting time was approximately 10 days.
* Appointment demand varied significantly between neighbourhoods.

### 8. Future Improvements

Potential improvements to the project include:

* Implementing automated AWS-based data ingestion.
* Introducing pipeline monitoring and error handling.
* Implementing automated data quality checks.
* Extending cloud integration with Amazon Aurora and Amazon Redshift.

⸻

Project: Healthcare Appointment Analysis Pipeline

Technologies: Python, Pandas, MySQL, SQL, DBeaver, Amazon S3, AWS Glue, Amazon Athena, Amazon Aurora, Amazon Redshift, Power BI, DAX, Git and GitHub.

Author: Omoefe Alicia Osayi