
import logging
from pathlib import Path

import boto3
import pandas as pd
from botocore.exceptions import ClientError, NoCredentialsError

# --------------------------------------------------
# Configuration
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "data" / "appointments.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "clean_appointments.csv"

BUCKET_NAME = "efe-healthcare-data-pipeline"
S3_KEY = "processed/clean_appointments.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# --------------------------------------------------
# Data Cleaning
# --------------------------------------------------

def clean_data():

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {INPUT_FILE}"
        )

    logger.info("Loading raw healthcare dataset")

    df = pd.read_csv(INPUT_FILE)

    original_rows = len(df)

    logger.info("Original records: %s", original_rows)

    required_columns = [
        "AppointmentID",
        "PatientId",
        "ScheduledDay",
        "AppointmentDay",
        "Age",
        "Gender",
        "No-show"
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # --------------------------------------------------
    # Missing Value Checks
    # --------------------------------------------------

    logger.info("Missing values before cleaning:")
    logger.info("\n%s", df.isnull().sum())

    # Remove records missing essential fields
    df = df.dropna(subset=required_columns).copy()

    # Convert Age to numeric
    df["Age"] = pd.to_numeric(
        df["Age"],
        errors="coerce"
    )

    df = df.dropna(subset=["Age"]).copy()

    # --------------------------------------------------
    # Remove Duplicate Appointments
    # --------------------------------------------------

    duplicate_count = df["AppointmentID"].duplicated().sum()

    df = df.drop_duplicates(
        subset="AppointmentID",
        keep="first"
    ).copy()

    logger.info(
        "Duplicate appointments removed: %s",
        duplicate_count
    )

    # --------------------------------------------------
    # Date Transformation
    # --------------------------------------------------

    df["ScheduledDay"] = pd.to_datetime(
        df["ScheduledDay"],
        errors="coerce"
    )

    df["AppointmentDay"] = pd.to_datetime(
        df["AppointmentDay"],
        errors="coerce"
    )

    # Remove records with invalid dates
    df = df.dropna(
        subset=["ScheduledDay", "AppointmentDay"]
    ).copy()

    # Calculate waiting time using calendar days
    df["DaysWaiting"] = (
        df["AppointmentDay"].dt.normalize()
        - df["ScheduledDay"].dt.normalize()
    ).dt.days

    # --------------------------------------------------
    # Data Validation
    # --------------------------------------------------

    invalid_age_count = (df["Age"] < 0).sum()

    df = df[df["Age"] >= 0].copy()

    negative_waiting_count = (
        df["DaysWaiting"] < 0
    ).sum()

    df = df[df["DaysWaiting"] >= 0].copy()

    logger.info("Invalid ages removed: %s", invalid_age_count)
    logger.info(
        "Negative waiting times removed: %s",
        negative_waiting_count
    )

    # --------------------------------------------------
    # Final Data Quality Checks
    # --------------------------------------------------

    if df["AppointmentID"].duplicated().any():
        raise ValueError("Duplicate appointment IDs detected")

    if (df["Age"] < 0).any():
        raise ValueError("Negative ages detected")

    if (df["DaysWaiting"] < 0).any():
        raise ValueError("Negative waiting times detected")

    if df[required_columns].isnull().any().any():
        raise ValueError("Missing essential values detected")

    logger.info("Data quality validation passed")

    # --------------------------------------------------
    # Save Cleaned Dataset
    # --------------------------------------------------

    df["ScheduledDay"] = df["ScheduledDay"].dt.strftime(
        "%Y-%m-%d"
    )

    df["AppointmentDay"] = df["AppointmentDay"].dt.strftime(
        "%Y-%m-%d"
    )

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(OUTPUT_FILE, index=False)

    cleaned_rows = len(df)

    logger.info("Data cleaning completed")
    logger.info("Original records: %s", original_rows)
    logger.info("Cleaned records: %s", cleaned_rows)
    logger.info(
        "Records removed: %s",
        original_rows - cleaned_rows
    )

    # --------------------------------------------------
    # Calculate No-show Rate
    # --------------------------------------------------

    no_show_rate = (
        df["No-show"].astype(str).str.strip().str.upper().eq("YES").mean()
        * 100
    )

    logger.info(
        "No-show rate: %.2f%%",
        no_show_rate
    )

    # --------------------------------------------------
    # Upload Cleaned Dataset to Amazon S3
    # --------------------------------------------------

    try:
        s3 = boto3.client("s3")

        s3.upload_file(
            str(OUTPUT_FILE),
            BUCKET_NAME,
            S3_KEY
        )

        logger.info(
            "Uploaded cleaned dataset to s3://%s/%s",
            BUCKET_NAME,
            S3_KEY
        )

    except NoCredentialsError:
        logger.exception("AWS credentials not configured")
        raise

    except ClientError:
        logger.exception("Failed to upload dataset to S3")
        raise

    return df


# --------------------------------------------------
# Main Execution
# --------------------------------------------------

if __name__ == "__main__":

    cleaned_df = clean_data()

    print("\nETL PROCESS COMPLETED")
    print(f"Final records: {len(cleaned_df)}")
