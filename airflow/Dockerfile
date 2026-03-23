FROM apache/airflow:2.10.0-python3.12

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir \
    "apache-airflow==2.10.0" \
    -r /requirements.txt \
    --constraint "${HOME}/constraints.txt"