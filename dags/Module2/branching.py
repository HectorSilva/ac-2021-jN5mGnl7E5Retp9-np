# pylint: disable=import-error
'''
My code
'''
import sys
sys.path.append("/opt/airflow/dags/Module2/dag_groups")
from datetime import datetime, timedelta
from taskgroups.tasks import process_tasks_dynamic
from airflow.decorators import (task, dag)
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import BranchPythonOperator

partners_info = {
    'partner_a': {
        'name': 'Bob',
        'path': '/usr/bin/bob'
    },
    'partner_b': {
        'name': 'Tim',
        'path': '/usr/bin/tim'
    },
    'partner_c': {
        'name': 'Prim',
        'path': '/usr/bin/prim'
    }
}

default_args = {
    'start_date': datetime(2021, 1, 1)
}


def _choosing_partner_based_on_day(execution_date):
    ''' This code shows the funcitonality of the PythonBranch Operator

    ARGS: execution_date
    '''
    day = execution_date.day_of_week
    if day == 1:  # Monday
        return 'extract_partner_a'  # task id de la tarea que quieres correr
    if day == 3:  # Wednesday
        return 'extract_partner_b'
    if day == 5:  # Friday
        return 'extract_partner_c'
    return 'stop'


@dag(description='DAG in charge to show how to do branching',
     default_args=default_args,
     schedule_interval='@daily',
     dagrun_timeout=timedelta(minutes=10),
     tags=['airflow',
           'branching',
           'advanced'],
     catchup=False,
     max_active_runs=1)
def branching_dag():
    ''' DAG to show how to branch tasks'''

    main = DummyOperator(task_id='main_task')

    choosing_partner_based_on_day = BranchPythonOperator(
        task_id='choosing_partner_based_on_day',
        python_callable=_choosing_partner_based_on_day
    )

    stop = DummyOperator(task_id='stop')

    storing = DummyOperator(
        task_id='storing',
        trigger_rule='none_failed_or_skipped')

    choosing_partner_based_on_day >> stop
    main >> choosing_partner_based_on_day
    for partner, details in partners_info.items():
        @task.python(task_id=f'extract_{partner}',
                     do_xcom_push=False, multiple_outputs=True)
        def extract(partner_name, partner_path):
            return {'name': partner_name, 'partner_path': partner_path}
        partners_settings = extract(details['name'], details['path'])
        main >> choosing_partner_based_on_day >> partners_settings
        process_tasks_dynamic(partners_settings) >> storing


dag = branching_dag()
