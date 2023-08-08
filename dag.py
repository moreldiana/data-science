import datetime as dt

from airflow import DAG
from airflow.operators.weekday import BranchDayOfWeekOperator
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2023, 8, 1),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

with DAG(
    dag_id='tester',
    default_args=default_args,
    schedule='@daily'
) as dag:


    daily_op = BashOperator(
        task_id='daily_task',
        bash_command='python  weather.py --approach daily',
    )

    daily_op