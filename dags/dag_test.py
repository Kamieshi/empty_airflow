from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'depends_on_past': False,
    'email': ['dmitry@platoteam.com'],
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG(f'test_empty_dag_tt',
          default_args=default_args,

          start_date=datetime(2022, 1, 1),
          catchup=False,
          schedule_interval=None
          )


def empty_fun():
    print('Hello from task')


empty_task = PythonOperator(task_id=f'empty_task',
                            python_callable=empty_fun,
                            provide_context=True,
                            dag=dag
                            )

empty_task
