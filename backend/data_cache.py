import os
import json
from pathlib import Path
from cryptography.fernet import Fernet

class DataCache:
    def __init__(self):
        self.cache_dir = Path('data/cache/')
        self.cache_dir.mkdir(exist_ok=True)
        self.encryption_key = Fernet.generate_key()  # Generate encryption key
        self.cipher = Fernet(self.encryption_key)

    def cache_data(self, data: dict, source: str):
        """Cache data locally"""
        encrypted_data = self.cipher.encrypt(json.dumps(data).encode())
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.cache_dir / f"{source}_{timestamp}.enc"
        
        with open(filename, 'wb') as f:
            f.write(encrypted_data)
        print(f"[CACHE] Data from {source} saved locally")

    def get_cached_data(self):
        """Get all cached files"""
        return [f for f in self.cache_dir.glob("*.enc")]

    def clear_cache(self):
        """Clear cache after sync"""
        for file in self.get_cached_data():
            os.remove(file)
        print("[CACHE] Cache cleared after successful sync")
