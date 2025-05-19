
# run.sh - Script to install and launch OpenSana on Raspberry Pi
# This script:
# - Creates necessary directories
# - Installs Python dependencies
# - Initializes Airflow
# - Starts Airflow scheduler
# - Launches the Dash dashboard
# - Runs background sync client

set -e  # Exit immediately if a command exits with a non-zero status

echo "🚀 Starting OpenSana setup..."

# --- Installing the working environment ---
echo "📁 Creating data directories..."
mkdir -p data/local_input data/processed data/cache

# Check install  Python3 and pip
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 not found. Install Python 3.9+"
    exit 1
fi

if ! command -v pip3 &> /dev/null
then
    echo "⚠️ pip3 not found. Try installing via: sudo apt install python3-pip"
    exit 1
fi

# --- Installing dependencies ---
echo "📦 Installing Python dependencies from requirements.txt..."
pip3 install -r requirements.txt

# --- Initializing Airflow ---
echo "⚙️ Initializing Apache Airflow database..."
airflow db init

# --- Run Airflow in the background ---
echo "🔄 Starting Airflow scheduler in background..."
nohup airflow scheduler > logs/airflow_scheduler.log 2>&1 &
echo "✅ Airflow scheduler started"

# --- Launching the dashboard ---
echo "📊 Starting Dash dashboard..."
python3 dashboard/app.py &
DASH_PID=$!
echo "✅ Dashboard is running on http://localhost:8050"

# --- Launching the ETL process ---
echo "🔁 Running Airflow standalone mode..."
python3 -m airflow standalone &
AIRFLOW_PID=$!
echo "✅ ETL engine started"

# --- Starting data synchronization ---
echo "📡 Starting offline data sync client..."
python3 backend/sync_client.py
echo "✅ Sync client is ready"

# --- Completion log ---
echo "🎉 OpenSana has been launched successfully!"
echo "🔗 Dashboard: http://localhost:8050"
echo "📘 To stop processes use kill $DASH_PID $AIRFLOW_PID"

exit 0
