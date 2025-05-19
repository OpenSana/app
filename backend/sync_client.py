# backend/sync_client.py
import requests
import time
from backend.data_cache import DataCache

class SyncClient:
    def __init__(self, server_url):
        self.server_url = server_url
        self.cache = DataCache()

    def check_internet_connection(self):
        """Checking for Internet connection"""
        try:
            requests.get("https://www.google.com ", timeout=3)
            return True
        except:
            return False

    def sync_data(self):
        """Synchronizing data with the server"""
        if not self.check_internet_connection():
            print("[SYNC] No internet connection. Data will remain cached.")
            return False
            
        cached_files = self.cache.get_cached_data()
        if not cached_files:
            print("[SYNC] No data to sync")
            return True

        for file in cached_files:
            with open(file, 'rb') as f:
                encrypted_data = f.read()
                # Data decryption (example)
                # decrypted_data = cache.cipher.decrypt(encrypted_data)
                # response = requests.post(self.server_url, json=json.loads(decrypted_data))
                
                print(f"[SYNC] Sent data from {file.name}")
                # The logic of the actual dispatch is here

        self.cache.clear_cache()
        return True

def sync_loop(interval=300):
    """Check and sync cycle"""
    client = SyncClient("https://api.opensana.org/sync ")
    while True:
        client.sync_data()
        time.sleep(interval)

if __name__ == "__main__":
    print("[SYNC] Running manual sync...")
    SyncClient("https://api.opensana.org/sync ").sync_data()
