# Data Pipeline
## Project summary
The main propurse of this project is to build a ETL pipeline of staging data (event and songs) from s3 to redshift, insert data into 1 fact table (songplay) and 4 dimension table (users, song, artist and time), then run data quality check, using airflow.
## DAGs
There are two DAGs:
- create_table_dag: This DAG is used to create tables which is one off. (workspace: airflow/dags/cd003-automate-data-pipelines/project/creat_tables_dag.py)
- final_project: This DAG is consist of staging staging data (event and songs) from s3 to redshift, inserting data into 1 fact table (songplay) and 4 dimension table (users, song, artist and time), then runing data quality check. This DAG is schedule to run every hour. (workspace: airflow/dags/cd003-automate-data-pipelines/project/starter/final_project.py)
## Operators:
- stag_redshift: Copy data from s3 to redshift
- load_fact: Insert into fact table
- load_dimension: Insert into dimension tables
- data_quality: Check row count
