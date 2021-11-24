import json
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.providers.http.sensors.http import HttpSensor


def _extract_data(**context):
    data = pd.read_html('https://en.wikipedia.org/wiki/List_of_cities_in_the_United_Kingdom')
    pass

def _transform_data(**context):
    pass
    
with DAG('example_etl', start_date=datetime(2020, 1, 1), schedule_interval=None) as dag:
    """Exercise: Create a DAG that uses the Bash operator in 5 tasks running different commands
    """
    
    service_is_available = HttpSensor(task_id="check_connection",
                                      endpoint='wiki/List_of_cities_in_the_United_Kingdom',
                                      method='GET',
                                      http_conn_id='wikipedia',
                                      response_check=lambda response: True if response.ok else False)
    