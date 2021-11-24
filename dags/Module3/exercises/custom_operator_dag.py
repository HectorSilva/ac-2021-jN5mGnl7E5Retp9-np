
import sys
sys.path.append("/opt/airflow/dags/Module3/exercises")
import requests
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('custom_operator', start_date=datetime(2020, 1, 1), schedule_interval=None) as dag:
    """Exercise: Create a DAG that uses the Bash operator in 5 tasks running different commands
    """
    pass
