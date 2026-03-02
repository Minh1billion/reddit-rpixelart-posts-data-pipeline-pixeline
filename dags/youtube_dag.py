import sys
sys.path.insert(0, '/opt/airflow')

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pipelines.youtube.fetcher import fetch_entries
from pipelines.youtube.loader import load

def run():
    entries = fetch_entries()
    if entries:
        load(entries)

with DAG(
    "youtube_thumbnails",
    schedule="0 * * * *",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    is_paused_upon_creation=False,
    tags=["youtube", "thumbnails"],
) as dag:

    task = PythonOperator(
        task_id="fetch_and_load",
        python_callable=run,
    )