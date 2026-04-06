# infrastructure/storage/worm_logger.py
"""
WORM Logger: Guarda logs forenses en Azure Blob Storage con política de inmutabilidad (WORM).
Formalizado para arquitectura enterprise.
"""
from azure.storage.blob import BlobServiceClient
from datetime import datetime, timedelta
import os
from core.utils import log_event

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "<your-connection-string>")
CONTAINER_NAME = "ares11-worm-logs"

def upload_worm_log(local_file: str, blob_name: str = None):
    if not blob_name:
        blob_name = os.path.basename(local_file)
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    container_client = blob_service_client.get_container_client(CONTAINER_NAME)
    try:
        container_client.create_container()
    except Exception:
        pass  # Ya existe
    blob_client = container_client.get_blob_client(blob_name)
    with open(local_file, "rb") as data:
        blob_client.upload_blob(
            data,
            overwrite=True,
            immutability_policy={
                "policy_mode": "Unlocked",
                "expiry_time": (datetime.utcnow() + timedelta(days=365)).isoformat()
            }
        )
    log_event("worm_log.uploaded", {"blob": blob_name})
    print(f"[WORM] Log forense subido a Azure Blob Storage: {blob_name} (inmutable)")
