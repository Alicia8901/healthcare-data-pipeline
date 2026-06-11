import pandas as pd

# Load raw dataset
df = pd.read_csv("../data/appointments.csv")

# Convert date columns
df["ScheduledDay"] = pd.to_datetime(df["ScheduledDay"]).dt.date
df["AppointmentDay"] = pd.to_datetime(df["AppointmentDay"]).dt.date

# Create DaysWaiting column
df["DaysWaiting"] = (
    pd.to_datetime(df["AppointmentDay"])
    - pd.to_datetime(df["ScheduledDay"])
).dt.days

# Remove invalid age values
df = df[df["Age"] >= 0]

# Remove negative waiting times
df = df[df["DaysWaiting"] >= 0]

# Save cleaned dataset
df.to_csv("../data/clean_appointments.csv", index=False)

print("Data cleaning complete!")
print(f"Rows remaining: {len(df)}")