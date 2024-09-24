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

### Getting Started

1. Clone the repository: `git clone https://github.com/mobatusi/formula-1-analysis-data-pipeline.git`
2. Install required dependencies: `pip install -r requirements.txt`
3. Set up BigQuery credentials: [follow instructions](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries)
4. Set up Apache Airflow: [follow instructions](https://airflow.apache.org/docs/apache-airflow/stable/installation.html)
5. Run the pipeline: `airflow db init` and `airflow scheduler`

### License

This repository is licensed under the [MIT License](https://opensource.org/licenses/MIT).

### Acknowledgments

* Kaggle Formula 1 World Championship (1950–2023) dataset
* Apache Airflow
* BigQuery