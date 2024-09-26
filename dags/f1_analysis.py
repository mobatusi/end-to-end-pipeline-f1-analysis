import os
import pandas as pd
import pendulum
from airflow.decorators import dag
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
    GCSToBigQueryOperator,BigQueryInsertJobOperator
)
from datetime import timedelta
from google.cloud import storage
import json

bucket_name = os.environ['GCS_BUCKET']
file_path = 'config.json'

# Create a client instance
client = storage.Client()

# Get the bucket
bucket = client.get_bucket(bucket_name)

# Get the blob
blob = bucket.blob(file_path)

# Download the blob as a string
config_str = blob.download_as_string().decode('utf-8')

# Load the JSON
config = json.loads(config_str)

# Access the parameters from the config
mybucket = config['mybucket']
dataset_id = config['dataset_id']
service_account_path = config['service_account_path']

PROJECT_ID = config['project_id']
SQL_FOLDER = "/sql"
DATA_FOLDER = "/data"

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': pendulum.duration(minutes=5),
}

@dag(
    schedule="* * * * 1-5",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=["educative"],
    template_searchpath=[SQL_FOLDER],
)
def f1_analysis_pipeline():
    ingestion = []

    # Create a task for each CSV file
    csv_files = ['drivers.csv', 'constructors.csv', 'races.csv', 'circuits.csv', 'results.csv']

    for file in csv_files:
        ingest_task = GCSToBigQueryOperator(
            task_id=f'ingest_{file}',
            bucket=mybucket,
            source_objects=[f'data/{file}'],
            destination_project_dataset_table=f'{PROJECT_ID}.{dataset_id}.{file.split(".")[0]}',
            source_format='CSV',
            create_disposition='CREATE_IF_NEEDED',
            write_disposition='WRITE_TRUNCATE',
        )
        # Add the task to the DAG
        ingestion.append(ingest_task)           