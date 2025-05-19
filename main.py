import os
from pathlib import Path
import sys

# Add the root folder to PYTHONPATH to import modules
sys.path.append(str(Path(__file__).parent))

# Init Airflow
from airflow.config.airflow_config import get_config as get_airflow_config
from airflow.models import DagBag

# Run dashboard
from dashboard.app import run_dashboard

# Working with data and caching
from backend.sync_client import sync_data_when_online

def start_app():
    """Start OpenSana application in offline-first mode."""
    print("[INFO] Starting OpenSana in offline mode...")

    # Getting Airflow settings
    config = get_airflow_config()
    print(f"[INFO] DAGs folder: {config['DAGS_FOLDER']}")

    # Checking DAGs
    dagbag = DagBag(config['DAGS_FOLDER'])
    if dagbag.import_errors:
        print("[ERROR] DAG Import Errors:", dagbag.import_errors)
    else:
        print("[INFO] All DAGs are ready.")

    # Launching a local dashboard
    print("[INFO] Starting local dashboard...")
    try:
        run_dashboard()
    except Exception as e:
        print(f"[ERROR] Failed to start dashboard: {e}")

    # Trying to sync when internet is available
    print("[INFO] Checking internet connection for data sync...")
    try:
        sync_data_when_online()
    except Exception as e:
        print(f"[ERROR] Data sync failed: {e}")

if __name__ == '__main__':
    start_app()
