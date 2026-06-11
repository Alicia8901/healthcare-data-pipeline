USE healthcare_appointments;

-- Verify that all cleaned records were successfully loaded into the database
SELECT COUNT(*) AS total_records
FROM appointments;

-- Verify the number of unique patients in the dataset
SELECT COUNT(DISTINCT PatientId) AS unique_patients
FROM appointments;

-- Verify that data cleaning removed negative waiting times
SELECT MIN(DaysWaiting) AS min_days_waiting,MAX(DaysWaiting) AS max_days_waiting
FROM appointments;

-- Calculate the average patient age
SELECT AVG(Age) AS average_age
FROM appointments;

-- Count appointments by gender
SELECT Gender, COUNT(*) AS total_appointments
FROM appointments
GROUP BY Gender;

-- Count attended versus missed appointments
SELECT `No-show`, COUNT(*) AS total_appointments
FROM appointments
GROUP BY `No-show`;

-- Calculate average waiting time by appointment outcome
SELECT `No-show`, AVG(DaysWaiting) AS average_waiting_time
FROM appointments
GROUP BY `No-show`;

-- Find the top 10 neighbourhoods by appointment volume
SELECT Neighbourhood, COUNT(*) AS total_appointments
FROM appointments
GROUP BY Neighbourhood
ORDER BY total_appointments DESC
LIMIT 10;
