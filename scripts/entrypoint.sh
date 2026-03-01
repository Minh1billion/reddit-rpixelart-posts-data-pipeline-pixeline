#!/bin/bash
set -e

case "$1" in
  init)
    echo "Initializing Airflow DB..."
    airflow db migrate
    airflow users create \
      --username admin \
      --password admin \
      --firstname Admin \
      --lastname Admin \
      --role Admin \
      --email admin@example.com || true
    echo "Init done."
    ;;
  webserver)
    exec airflow webserver
    ;;
  scheduler)
    exec airflow scheduler
    ;;
  *)
    exec "$@"
    ;;
esac