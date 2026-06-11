USE healthcare_appointments;

-- Summary of appointment outcomes
CREATE VIEW appointment_outcomes AS
SELECT `No-show`, COUNT(*) AS total_appointments
FROM appointments
GROUP BY `No-show`;

-- Average waiting time by appointment outcome
CREATE VIEW waiting_time_summary AS
SELECT `No-show`, AVG(DaysWaiting) AS average_waiting_time
FROM appointments
GROUP BY `No-show`;

-- Appointments by gender
CREATE VIEW gender_summary AS
SELECT Gender, COUNT(*) AS total_appointments
FROM appointments
GROUP BY Gender;