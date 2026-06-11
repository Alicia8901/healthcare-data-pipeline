CREATE DATABASE healthcare_appointments;
USE healthcare_appointments;


CREATE TABLE appointments (
    PatientId BIGINT,
    AppointmentID BIGINT PRIMARY KEY,
    Gender VARCHAR(10),
    ScheduledDay DATE,
    AppointmentDay DATE,
    Age INT,
    Neighbourhood VARCHAR(100),
    Scholarship INT,
    Hipertension INT,
    Diabetes INT,
    Alcoholism INT,
    Handicap INT,
    SMS_received INT,
    `No-show` VARCHAR(10),
    DaysWaiting INT
);


