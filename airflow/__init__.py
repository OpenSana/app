from airflow import settings
from airflow.models import DagBag

def init_airflow():
    """
    Initialize Airflow environment.
    Creates DB and loads DAGs.
    """
    print("[AIRFLOW] Initializing Airflow")
    settings.configure_orm()
    dagbag = DagBag(os.path.join(os.getcwd(), 'airflow/dags'))
    if dagbag.import_errors:
        print("[ERROR] DAG Import Errors:", dagbag.import_errors)
