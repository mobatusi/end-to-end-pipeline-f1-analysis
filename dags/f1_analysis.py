import os
import pandas as pd
import pendulum
from airflow.decorators import dag, task
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from google.cloud import bigquery

#### SETUP: 
##   1. Save your GOOGLE_APPLICATION_CREDENTIALS into /usercode/auth.json 
##   2. Provide your PROJECT_ID
####
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/usercode/auth.json"
PROJECT_ID = "<YOUR_PROJECT_ID>"
SQL_FOLDER = "/usercode/sql"
DATA_FOLDER = "/usercode/data"

