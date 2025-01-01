from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define the DAG configuration
default_args = {
    'owner': 'airflow',
    'start_date': datetime.now(),
    'catchup': False,
}

with DAG('hello', default_args=default_args, schedule_interval='@daily') as dag:
    # Define the tasks
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        bash_command='sleep 5',
    )

    t3 = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello World"',
    )

# Define the task dependencies
t1 >> t2 >> t3