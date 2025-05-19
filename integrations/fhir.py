from fhirclient.models.patient import Patient
from fhirclient.models.observation import Observation
from backend.data_cache import DataCache

class FHIRClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.cache = DataCache()
    
    def export_fhir_patient(self, patient_data):
        """Converting data to FHIR format"""
        patient = Patient()
        patient.name = [{'text': patient_data['name']}]
        patient.gender = patient_data['gender']
        return patient.as_json()

    def store_locally(self, data, filename):
        """Saving in FHIR format locally"""
        with open(f"data/local_input/{filename}.json", "w") as f:
            f.write(data)
        self.cache.cache_data(data, 'fhir')

    def sync_with_server(self):
        """Synchronization with FHIR server"""
        pass  # Implemented with internet access

if __name__ == "__main__":
    client = FHIRClient("http://fhir.example.org")
    sample = {
        "name": "Patient/John Doe",
        "gender": "male"
    }
    fhir_data = client.export_fhir_patient(sample)
    client.store_locally(fhir_data, "patient_123")
