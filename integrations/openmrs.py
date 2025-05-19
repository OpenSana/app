import requests
from backend.data_cache import DataCache

class OpenMRSClinic:
    def __init__(self, base_url, user, pwd):
        self.base_url = base_url
        self.auth = (user, pwd)
        self.cache = DataCache()

    def fetch_patients(self):
        """Getting a list of patients"""
        try:
            res = requests.get(f"{self.base_url}/openmrs/ws/rest/v1/patient", auth=self.auth)
            return res.json()
        except:
            print("[OpenMRS] Offline — fetching local data")
            return self.cache.get_cached_data()

    def upload_observation(self, obs_data):
        """Loading observations"""
        try:
            res = requests.post(f"{self.base_url}/openmrs/ws/rest/v1/obs", json=obs_data, auth=self.auth)
            return res.status_code == 201
        except:
            self.cache.cache_data(obs_data, 'openmrs')
            return False

if __name__ == "__main__":
    clinic = OpenMRSClinic("http://openmrs.example.org", "admin", "Admin123")
    clinic.upload_observation({"concept": "HIV", "value": "Positive"})
