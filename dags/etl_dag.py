from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2026, 4, 1),
    'retries': 1
}

dag = DAG(
    's3_spark_etl_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False
)

run_spark_job = BashOperator(
    task_id='run_spark_etl',
    bash_command='spark-submit --packages org.apache.hadoop:hadoop-aws:3.3.1 /home/ubuntu/etl_spark_job.py',
    dag=dag
)

run_spark_job
