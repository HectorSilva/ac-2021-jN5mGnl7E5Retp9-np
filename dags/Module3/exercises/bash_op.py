from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('example_secrets_dags', start_date=datetime(2020, 1, 1), schedule_interval=None) as dag:
    """Exercise: Create a DAG that uses the Bash operator in 5 tasks running different commands
    """
    pass