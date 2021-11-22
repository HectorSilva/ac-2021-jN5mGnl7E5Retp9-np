from airflow.decorators import dag, task
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

@dag(schedule_interval='@daily', start_date=datetime(2021, 1, 1), catchup=False, tags=['first_project'])
def first_dag():
    """
    DAG to send server IP to email.

    :param email: Email to send IP to. Defaults to example@example.com.
    :type email: str
    """
    dummy_task = DummyOperator(task_id='dumy_task')


dag = first_dag()