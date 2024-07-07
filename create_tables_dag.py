import pendulum

from airflow import DAG
from airflow.secrets.metastore import MetastoreBackend
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

from udacity.common import sql_statements



dag = DAG(
    'create_table_dag',
    start_date=pendulum.now()
)

drop_staging_events_table = PostgresOperator(
    task_id="drop_staging_events_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.staging_events_table_drop
)

drop_staging_songs_table = PostgresOperator(
    task_id="drop_staging_song_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.staging_songs_table_drop
)

drop_songplay_table = PostgresOperator(
    task_id="drop_songplay_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.songplay_table_drop
)

drop_user_table = PostgresOperator(
    task_id="drop_user_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.user_table_drop
)

drop_song_table = PostgresOperator(
    task_id="drop_song_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.song_table_drop
)

drop_artist_table = PostgresOperator(
    task_id="create_artist_drop",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.artist_table_drop
)

drop_time_table = PostgresOperator(
    task_id="drop_time_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.time_table_drop
)



create_staging_events_table = PostgresOperator(
    task_id="create_staging_events_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.staging_events_table_create
)

create_staging_songs_table = PostgresOperator(
    task_id="create_staging_song_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.staging_songs_table_create
)

create_songplay_table = PostgresOperator(
    task_id="create_songplay_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.songplay_table_create
)

create_user_table = PostgresOperator(
    task_id="create_user_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.user_table_create
)

create_song_table = PostgresOperator(
    task_id="create_song_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.song_table_create
)

create_artist_table = PostgresOperator(
    task_id="create_artist_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.artist_table_create
)

create_time_table = PostgresOperator(
    task_id="create_time_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=sql_statements.time_table_create
)



drop_staging_events_table >> drop_staging_songs_table >> drop_songplay_table >> drop_user_table >> drop_song_table >> drop_artist_table >> drop_time_table >> create_staging_events_table >> create_staging_songs_table >> create_songplay_table >> create_user_table >> create_song_table >> create_artist_table >> create_time_table











