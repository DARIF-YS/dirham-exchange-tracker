from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../pipeline')))

from extract import Extract
from transform import Transform
from load import Load

# Définir le DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 5, 1),
    'retries': 1,
}

with DAG(
    dag_id='etl_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    description='Pipeline ETL quotidien : extract, transform et load des données brutes.',
    tags=['etl', 'pipeline', 'devise'],
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=Extract,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=Transform,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=Load,
    )

    extract_task >> transform_task >> load_task
