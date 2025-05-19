"""
Global settings for the OpenSana platform.
Designed for offline-first operation on lightweight devices like Raspberry Pi.
"""

import os
from pathlib import Path

# Work mode
RASPBERRY_PI_MODE = True
ENABLE_INTERNET_CHECK = True

# Data Paths
LOCAL_DATA_PATH = "data/local_input/"
PROCESSED_DATA_PATH = "data/processed/"
CACHE_PATH = "data/cache/"

# Create directories if they do not exist
for path in [LOCAL_DATA_PATH, PROCESSED_DATA_PATH, CACHE_PATH]:
    Path(path).mkdir(parents=True, exist_ok=True)

# Authorization in systems (offline mode)
OFFLINE_CREDENTIALS = {
    'dhis2': {'username': 'offline', 'password': 'localonly'},
    'openmrs': {'username': 'offline', 'password': 'localonly'}
}

# Device name (for logging)
DEVICE_ID = os.getenv("DEVICE_ID", "default_rpi_device")

# Local server (for tests)
LOCAL_SERVER_PORT = 8050

# Logging level
LOG_LEVEL = "INFO"
DEBUG_MODE = False

# Temporary data storage format
DATA_STORAGE_FORMAT = "CSV"  # : CSV, JSON, Parquet

# Time between internet checks (in seconds)
SYNC_INTERVAL = 300  # 5 min
