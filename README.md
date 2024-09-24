# end-to-end-pipeline-f1-analysis

## End-to-End Data Pipeline for Formula 1 Analysis README

### Overview

This repository contains a production-grade end-to-end data pipeline for analyzing Formula 1 World Championship data. The pipeline ingests source data into a BigQuery data warehouse, transforms the data using SQL, and schedules the pipeline using Apache Airflow.

### Requirements

* Ingest source data into BigQuery data warehouse
* Design a data warehouse using Kimball data modeling techniques
* Transform data using SQL to answer analytical questions
* Schedule data pipeline using Apache Airflow

### Source Data

The source data comes from the Kaggle Formula 1 World Championship (1950–2023) dataset. The following CSV files are used:

* `drivers.csv`: Information about F1 drivers
* `constructors.csv`: Information about F1 constructors
* `races.csv`: Information about races in F1
* `circuitid.csv`: Information about circuits where F1 races are held
* `results.csv`: Information about results of F1 races

### Analytical Questions

The pipeline is designed to answer the following analytical questions:

* How many points does constructor Red Bull make in the year 2019?
* Which driver gets the most points from the year 2018 to 2020?
* Which circuit does driver Lewis Hamilton win the most?

### Pipeline Components

* **Data Ingestion**: Ingests source data into BigQuery data warehouse
* **Data Transformation**: Transforms data using SQL to answer analytical questions
* **Data Scheduling**: Schedules data pipeline using Apache Airflow

### Setup Instructions

1. **Generate GCP Credentials**:
   - Follow the steps to create a service account:
     - Log in to the Google Cloud Console.
     - Go to **IAM & Admin** > **Service accounts** > **+ Create Service Account**[1][4].
     - Enter a service account name, ID, and description.
     - Click **Create** and then **Done**.
     - Create a new key for the service account:
       - Go to **IAM & Admin** > **Service accounts** > **Manage keys**.
       - Click **Add Key** > **Create new key**.
       - Select **JSON** as the key type and click **Create**.
       - Save the downloaded JSON key file securely.

2. **Assign Roles to the Service Account**:
   - Grant the necessary roles to the service account:
     - Go to **IAM & Admin** > **IAM**.
     - Click **Add**.
     - Paste the email address of the service account.
     - Select the appropriate roles (e.g., **BigQuery Admin**, **Cloud Storage Admin**, **Cloud Composer Service Agent**).
     - Click **Save**

3. **Create BigQuery Dataset**:
   - Go to the BigQuery console.
   - Click the “⋮” icon next to the project name.
   - Click “Create dataset” and provide dataset ID “f1_analysis.”
   - Click the “Create dataset” button.

4. **Review Directory Structure**:
   - The repository includes the following directories:
     - `dags`: Contains the Airflow DAGs.
     - `sql`: Contains the necessary SQL files for the DAGs.
     - `data`: Contains the required input data in CSV format.

5. **Setup Cloud Composer**:
   - Create a Cloud Composer environment:
     - Go to the Google Cloud Console.
     - Navigate to **Cloud Composer** > **Environments**.
     - Click **Create**.
     - Follow the instructions to create a new environment.
   - Configure the service account in Cloud Composer:
     - Go to **Cloud Composer** > **Environments** > **Your Environment**.
     - Click **Edit**.
     - Under **Service account**, select the service account created earlier.
     - Click **Save**.

### Getting Started

1. Clone the repository: `git clone https://github.com/mobatusi/formula-1-analysis-data-pipeline.git`
2. Install required dependencies: `pip install -r requirements.txt`
3. Set up BigQuery credentials as described above.
4. Set up Apache Airflow: [follow instructions](https://airflow.apache.org/docs/apache-airflow/stable/installation.html)
5. Run the pipeline: `airflow db init` and `airflow scheduler`

### Getting Started

1. Clone the repository.
2. Set up BigQuery credentials as described above.
3. Set up Cloud Composer.
4. Run the pipeline using Cloud Composer.

### License

This repository is licensed under the [MIT License](https://opensource.org/licenses/MIT).

### Acknowledgments

* Kaggle Formula 1 World Championship (1950–2023) dataset
* Apache Airflow
* BigQuery