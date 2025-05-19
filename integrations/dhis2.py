import requests
from backend.data_cache import DataCache

class DHIS2Client:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.auth = (username, password)
        self.cache = DataCache()
    
    def fetch_metadata(self):
        """Getting DHIS2 Metadata"""
        try:
            res = requests.get(f"{self.base_url}/api/organisationUnits", auth=self.auth)
            return res.json()
        except Exception as e:
            print(f"[DHIS2] Error fetching metadata: {e}")
            return None
    
    def store_data(self, data):
        """Saving data locally"""
        self.cache.cache_data(data, 'dhis2')

    def push_data(self, endpoint):
        """Attempting to send data to DHIS2"""
        if not self.cache.get_cached_data():
            print("[DHIS2] No cached data to push")
            return
        
        # Демонстрация интеграции
        print(f"[DHIS2] Pushing data to {endpoint}")

if __name__ == "__main__":
    client = DHIS2Client("https://dhis2.example.org ", "admin", "district")
    metadata = client.fetch_metadata()
    client.store_data(metadata)
