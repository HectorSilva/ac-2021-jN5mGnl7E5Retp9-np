from airflow.models import DAG
from airflow.models.baseoperator import cross_downstream, chain
from airflow.utils.edgemodifier import Label
from airflow.operators.dummy import DummyOperator
from datetime import datetime

with DAG(dag_id='chain',
         schedule_interval='@daily',
         description='How to use chains',
         start_date=datetime(2021, 1, 1),
         tags=['Chain'],
         catchup=False) as dag:
    
    t1 = DummyOperator(task_id='t1')
    t2 = DummyOperator(task_id='t2')
    t3 = DummyOperator(task_id='t3')
    t4 = DummyOperator(task_id='t4')
    t5 = DummyOperator(task_id='t5')
    t6 = DummyOperator(task_id='t6')
    t7 = DummyOperator(task_id='t7')
    
    chain(t1, [t2, t3], [Label('Dependencia1'), Label('Dependencia2')] ,[t4, t6], Label('My dependency'), t7, t5)