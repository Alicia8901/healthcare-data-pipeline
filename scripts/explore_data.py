import pandas as pd

# Load the dataset from the data folder
df = pd.read_csv("../data/appointments.csv")

# Display the first 5 rows to understand the structure
print("First 5 Rows:")
print(df.head())

# Check number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# View all column names
print("\nColumn Names:")
print(df.columns)

# Check data types and non-null values
print("\nDataset Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Generate summary statistics for Age
print("\nAge Statistics:")
print(df["Age"].describe())

# Count attended vs missed appointments
print("\nNo-show Counts:")
print(df["No-show"].value_counts())

# Calculate no-show percentages
print("\nNo-show Percentages:")
print((df["No-show"].value_counts(normalize=True) * 100).round(2))

# Find records with invalid ages
print("\nInvalid Ages:")
print(df[df["Age"] < 0])

# Convert date columns from text to datetime
df["ScheduledDay"] = pd.to_datetime(df["ScheduledDay"]).dt.date
df["AppointmentDay"] = pd.to_datetime(df["AppointmentDay"]).dt.date

# Create waiting time feature
df["DaysWaiting"] = (
    pd.to_datetime(df["AppointmentDay"])
    - pd.to_datetime(df["ScheduledDay"])
).dt.days

# Check waiting time statistics
print("\nDays Waiting Statistics:")
print(df["DaysWaiting"].describe())

# Identify records with negative waiting times
print("\nNegative Waiting Times:")
print(df[df["DaysWaiting"] < 0])

# Calculate average waiting time for attendees vs no-shows
print("\nAverage Waiting Time by No-show Status:")
print(df.groupby("No-show")["DaysWaiting"].mean())