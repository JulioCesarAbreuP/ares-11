from azure.storage.blob import BlobServiceClient, ContentSettings
import os

def upload_immutable_evidence(file_path, connection_string, container_name):
    """
    Sube el log forense a un contenedor con 'WORM' activado.
    Incluso con llaves de admin, no se puede borrar hasta que expire el plazo.
    """
    client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = client.get_blob_client(container=container_name, blob=os.path.basename(file_path))
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=False, content_settings=ContentSettings(content_type='text/plain'))
    print(f"[✓] EVIDENCIA PROTEGIDA: {file_path} ahora es inmutable en Azure.")
