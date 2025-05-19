# airflow/dags/etl_pipeline.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import os

def extract_local_data(**kwargs):
    """Extracting data from a device"""
    data_path = "data/local_input/"
    dfs = []
    for file in os.listdir(data_path):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(data_path, file))
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True) if dfs else None

def transform_data(**kwargs):
    """Data transformation"""
    ti = kwargs['ti']
    raw_data = ti.xcom_pull(task_ids='extract_data')
    
    if raw_data is None:
        print("[ETL] No data to transform")
        return
    
    # Conversion example
    transformed = raw_data.fillna(0).astype(int)
    transformed.to_csv("data/processed/latest_transformed.csv", index=False)
    return transformed

def load_to_cache(**kwargs):
    """Save to cache before synchronization"""
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(task_ids='transform_data')
    
    if transformed_data is None:
        print("[ETL] No data to cache")
        return
    
    transformed_data.to_csv("data/cache/offline_export.csv", index=False)
    print("[ETL] Data cached locally")

default_args = {
    'owner': 'OpenSana',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('opensana_etl', default_args=default_args, schedule=timedelta(hours=1))
