FROM apache/airflow:2.2.5-python3.8
RUN pip install apache-airflow-providers-snowflake
RUN pip install pandas