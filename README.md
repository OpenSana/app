# OpenSana – Offline-First Health Data Platform

## Overview
OpenSana is an open-source platform for collecting, analyzing, and visualizing public health data in low-resource environments.
It works without internet, runs on Raspberry Pi, and integrates with DHIS2, FHIR, and OpenMRS.

## Repository
[GitHub Link](https://github.com/opensana/app)

## Project Structure

```
opensana/
├── backend/
│   ├── data_cache.py       # Local data caching for offline mode
│   └── sync_client.py      # Data sync when internet is available
├── airflow/
│   ├── dags/
│   │   └── etl_pipeline.py # ETL pipeline using Apache Airflow
│   └── config/
│       └── airflow_config.py # Airflow settings
├── dashboard/
│   ├── app.py              # Dash dashboard entry point
│   └── visualize.py        # Visualization logic with Plotly
├── integrations/
│   ├── dhis2.py            # DHIS2 API integration
│   ├── fhir.py             # FHIR standards support
│   └── openmrs.py          # OpenMRS system integration
├── config/
│   └── settings.py         # Global application settings
├── data/
│   └── sample_data.csv     # Sample dataset for testing
├── scripts/
│   └── run.sh              # Raspberry Pi launch script
├── README.md               # This file
├── requirements.txt        # Python dependencies
└── main.py                 # Application entry point
```

---

## ⚙️ Installation on Raspberry Pi

### 1. Clone the repository:
```
bash
git clone https://github.com/opensana/app.git 
cd opensana
```
### 2. Install dependencies and run:
```
chmod +x scripts/run.sh
./scripts/run.sh
```
✅ This script: 
  - Creates required directories (data/cache/, data/local_input/)
  - Installs Python packages from requirements.txt
  - Initializes Airflow database
  - Starts Airflow scheduler in background
  - Launches Dash dashboard on port 8050
  - Runs offline sync client

## 🧩 What Needs Implementation (for future PRs)
| FILE  | TASK |
| ------------- | ------------- |
| main.py  | Import modules from ```config/settings.py```  |
| main.py  | Handle DAGBag initialization errors  |
| main.py  | Run components in background processes  |
| airflow/dags/etl_pipeline.py  | Implement data processing logic  |
| airflow/dags/etl_pipeline.py  | Add ```CSV/JSON``` support from ```data/local_input/```  |
| airflow/dags/etl_pipeline.py  | Save processed data to ```data/processed/```  |
| dashboard/app.py  | Add login/auth for local dashboard  |
| dashboard/app.py  | Enable chart export as ```PNG/PDF```  |
| dashboard/app.py  | Support dynamic data reloading  |
| dashboard/visualize.py  | Add map/heatmap/table chart types  |
| dashboard/visualize.py  | Improve mobile responsiveness  |
| dashboard/visualize.py  | Add visual export options  |
| backend/data_cache.py  | Implement encrypted local storage  |
| backend/data_cache.py  | Add cache expiration policy  |
| backend/data_cache.py  | Add caching logic unit tests  |
| backend/sync_client.py  | Add sync retry logic  |
| backend/sync_client.py  | Implement batch sync for large datasets  |
| backend/sync_client.py  | Add sync attempt logging  |
| integrations/dhis2.py  | Add full DHIS2 CRUD support  |
| integrations/dhis2.py  | Implement metadata sync  |
| integrations/dhis2.py  | Add API change error handling  |
| integrations/fhir.py  | Add FHIR resource validation  |
| integrations/fhir.py  | Implement smart search/filtering  |
| integrations/fhir.py  | Add FHIR bundle support  |
| integrations/openmrs.py  | Add patient/observation sync  |
| integrations/openmrs.py  | Implement offline sync queue  |
| integrations/openmrs.py  | Support legacy OpenMRS versions  |
| airflow/config/airflow_config.py  | Add SQLite → PostgreSQL switch  |
| airflow/config/airflow_config.py  | Implement DAG versioning  |
| airflow/config/airflow_config.py  | Add logging configuration  |
| config/settings.py  | Add ```.env``` file support  |
| config/settings.py  | Add configurable sync interval  |
| config/settings.py  | Implement device ID auto-generation  |
| scripts/run.sh  | Add missing file error handling  |
| scripts/run.sh  | Add auto-restart on failure  |
| scripts/run.sh  | Implement log rotation  |

## 📊 How to Use
1. Add CSV files to data/local_input/
2. DAGs will process them automatically
3. Open dashboard at http://localhost:8050
4. Data will sync via backend/sync_client.py when internet becomes available

## 🤝 Contributing
All contributions are welcome!
Fork the project and submit a PR with your changes.
Use the task list above to find a starting point.

## 📄 License
MIT License
See LICENSE for details.
