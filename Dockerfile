FROM apache/airflow:2.8.0

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

USER airflow
COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

COPY core/ /opt/airflow/core/
COPY pipelines/ /opt/airflow/pipelines/
COPY dags/ /opt/airflow/dags/
COPY /scripts/entrypoint.sh entrypoint.sh

USER root
RUN chmod +x entrypoint.sh

USER airflow
ENTRYPOINT ["/entrypoint.sh"]