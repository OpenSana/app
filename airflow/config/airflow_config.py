
"""
Configuration file for Apache Airflow in offline-first mode.
Designed to work with OpenSana on Raspberry Pi devices.
"""

import os
from pathlib import Path

# Basic Airflow settings
AIRFLOW_HOME = os.getenv("AIRFLOW_HOME", str(Path(__file__).parent.parent.parent))
DAGS_FOLDER = os.path.join(AIRFLOW_HOME, "airflow", "dags")
PLUGINS_FOLDER = os.path.join(AIRFLOW_HOME, "airflow", "plugins")

# Database (SQLite - for offline mode)
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(AIRFLOW_HOME, 'airflow.db')}"

#The default parameters for DAG
DEFAULT_ARGS = {
    "owner": "OpenSana",
    "depends_on_past": False,
    "start_date": "2025-01-01",
    "email": ["team@opensana.org"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": "timedelta(minutes=5)",
}

# Default DAG Startup Interval
DEFAULT_SCHEDULE_INTERVAL = "None  # Manual or event triggered"

# Logging and basic setup
LOGGING_LEVEL = "INFO"
ENABLE_XCOM_PICKLING = True

# Data Paths
INPUT_DATA_PATH = os.path.join(AIRFLOW_HOME, "data/local_input/")
PROCESSED_DATA_PATH = os.path.join(AIRFLOW_HOME, "data/processed/")
CACHE_DATA_PATH = os.path.join(AIRFLOW_HOME, "data/cache/")

# Security settings
LOAD_EXAMPLES = False
SECURE_MODE = True

def get_config():
    """Return all settings as a dict"""
    return {
        "AIRFLOW_HOME": AIRFLOW_HOME,
        "DAGS_FOLDER": DAGS_FOLDER,
        "SQLALCHEMY_DATABASE_URI": SQLALCHEMY_DATABASE_URI,
        "DEFAULT_ARGS": DEFAULT_ARGS,
        "DEFAULT_SCHEDULE_INTERVAL": DEFAULT_SCHEDULE_INTERVAL,
        "INPUT_DATA_PATH": INPUT_DATA_PATH,
        "PROCESSED_DATA_PATH": PROCESSED_DATA_PATH,
        "CACHE_DATA_PATH": CACHE_DATA_PATH,
        "LOGGING_LEVEL": LOGGING_LEVEL,
        "ENABLE_XCOM_PICKLING": ENABLE_XCOM_PICKLING,
        "SECURE_MODE": SECURE_MODE
    }
