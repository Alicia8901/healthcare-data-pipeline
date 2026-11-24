import boto3
from pathlib import Path
from botocore.exceptions import ClientError, NoCredentialsError

BUCKET_NAME = "efe-healthcare-data-pipeline"
LOCAL_FILE = Path("data/appointments.csv")
S3_KEY = "raw/appointments.csv"


def upload_file():
    if not LOCAL_FILE.exists():
        print(f"Error: File not found: {LOCAL_FILE}")
        return

    try:
        s3 = boto3.client("s3")

        s3.upload_file(
            str(LOCAL_FILE),
            BUCKET_NAME,
            S3_KEY
        )

        print("Upload successful!")
        print(f"Bucket: {BUCKET_NAME}")
        print(f"File: {S3_KEY}")

    except NoCredentialsError:
        print("Error: AWS credentials not configured.")

    except ClientError as error:
        print(f"AWS upload failed: {error}")


if __name__ == "__main__":
    upload_file()
