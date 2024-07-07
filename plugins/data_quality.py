from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 conn_id,
                 tables,
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.conn_id = conn_id
        self.tables = tables

    def execute(self, context):
        redshift_hook = PostgresHook(self.conn_id)
        for table in self.tables:
            records = redshift_hook.get_records(f'SELECT COUNT(*) FROM {table}')
            if len(records) < 1 or len(records[0]) < 1:
                raise ValueError(f"Data quality check failed. There's no result in {table}")
            if records[0][0] < 1:
                raise ValueError(f"Data quality check failed. {table} conains 0 rows")
            self.log.info(f'Data quality check passed: {table} has {records[0][0]} records')



   
