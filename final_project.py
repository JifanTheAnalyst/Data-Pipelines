from datetime import datetime, timedelta
import pendulum
import os
from airflow import DAG
from airflow.decorators import dag
from airflow.operators.dummy_operator import DummyOperator
from final_project_operators.stage_redshift import StageToRedshiftOperator
from final_project_operators.load_fact import LoadFactOperator
from final_project_operators.load_dimension import LoadDimensionOperator
from final_project_operators.data_quality import DataQualityOperator
from udacity.common.final_project_sql_statements import SqlQueries




default_args = {
    'owner': 'JIFAN',
    'start_date': pendulum.now(),
    'depends_on_past': False,
    'retries':3,
    'retry_delay':timedelta(minutes=5),
    'catchup':False
}


dag = DAG('final_project',
    default_args=default_args,
    description='Load and transform data in Redshift with Airflow',
    schedule_interval='0 * * * *')

start_operator = DummyOperator(task_id='Begin_execution', dag=dag)

stage_events_to_redshift = StageToRedshiftOperator(
    task_id='Stage_events',
    dag=dag,
    table='staging_events',
    conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="jiffyjanicebucket",
    s3_key="log-data",
    json_path='s3://jiffyjanicebucket/log_json_path.json'
)

stage_songs_to_redshift = StageToRedshiftOperator(
    task_id='Stage_songs',
    dag=dag,
    table='staging_songs',
    conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="jiffyjanicebucket",
    s3_key="song-data",
    json_path='auto'
)

load_songplays_table = LoadFactOperator(
    task_id='Load_songplays_fact_table',
    dag=dag,
    conn_id="redshift",
    table='songplay',
    query=SqlQueries.songplay_table_insert
)

load_user_dimension_table = LoadDimensionOperator(
    task_id='Load_user_dim_table',
    dag=dag,
    conn_id="redshift",
    table='users',
    query=SqlQueries.user_table_insert,
    truncate=True
)

load_song_dimension_table = LoadDimensionOperator(
    task_id='Load_song_dim_table',
    dag=dag,
    conn_id="redshift",
    table='song',
    query=SqlQueries.song_table_insert,
    truncate=True
)

load_artist_dimension_table = LoadDimensionOperator(
    task_id='Load_artist_dim_table',
    dag=dag,
    conn_id="redshift",
    table='artist',
    query=SqlQueries.artist_table_insert,
    truncate=True
)

load_time_dimension_table = LoadDimensionOperator(
    task_id='Load_time_dim_table',
    dag=dag,
    conn_id="redshift",
    table='time',
    query=SqlQueries.time_table_insert,
    truncate=True
)

run_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    conn_id="redshift",
    tables=['song', 'users', 'artist', 'time'],
    dag=dag
)
end_operator = DummyOperator(task_id='Stop_execution', dag=dag)

start_operator >> stage_events_to_redshift
start_operator >> stage_songs_to_redshift

stage_events_to_redshift >> load_songplays_table
stage_songs_to_redshift >> load_songplays_table

load_songplays_table >> load_song_dimension_table
load_songplays_table >> load_user_dimension_table
load_songplays_table >> load_artist_dimension_table
load_songplays_table >> load_time_dimension_table
    

load_song_dimension_table >> run_quality_checks
load_user_dimension_table >> run_quality_checks
load_artist_dimension_table >> run_quality_checks
load_time_dimension_table >> run_quality_checks

run_quality_checks >> end_operator
