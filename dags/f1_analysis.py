import os
import pendulum
from airflow import DAG
from airflow.decorators import dag, task
from airflow.models import Variable
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
    GCSToBigQueryOperator,
)
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.models.baseoperator import chain

# Replace module-level code with Airflow Variables
GCS_BUCKET = os.environ['GCS_BUCKET']
DATASET_ID = os.environ['dataset_id']
PROJECT_ID = os.environ['GCP_PROJECT']

@dag(
    schedule="0 0 * * 1-5",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
    tags=["educative"],
)
def f1_analysis_pipeline():
    # Create a task for each CSV file
    csv_files = ['drivers.csv', 'constructors.csv', 'races.csv', 'circuits.csv', 'results.csv']

    # Data ingestion tasks
    ingestion_tasks = []
    for file in csv_files:
        ingest_task = GCSToBigQueryOperator(
            task_id=f'ingest_{file}',
            bucket=GCS_BUCKET,
            source_objects=[f'data/{file}'],
            destination_project_dataset_table=f'{PROJECT_ID}.{DATASET_ID}.{file.split(".")[0]}',
            source_format='CSV',
            skip_leading_rows=1,  # Skip header row if CSV includes headers
            autodetect=True,      # Let BigQuery autodetect the schema
            create_disposition='CREATE_IF_NEEDED',
            write_disposition='WRITE_TRUNCATE',
        )
        # Add the task to the DAG
        ingestion_tasks.append(ingest_task)              
    
    # Read SQL content from GCS
    @task
    def read_sql_from_gcs():
        from google.cloud import storage
        client = storage.Client()
        bucket = client.bucket(GCS_BUCKET)
        blob = bucket.blob('sql/f1_analysis.sql')
        sql_content = blob.download_as_text()
        return sql_content

    # Run the BigQuery job
    @task
    def run_f1_analysis(sql_content):
        from google.cloud import bigquery
        client = bigquery.Client()
        job = client.query(sql_content)
        job.result()  # Wait for the job to complete
    
    sql_content = read_sql_from_gcs()
    run_analysis = run_f1_analysis(sql_content)

    # Set task dependencies
    ingestion_tasks >> sql_content >> run_analysis

f1_analysis_pipeline()