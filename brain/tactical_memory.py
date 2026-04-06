import chromadb
from chromadb.utils import embedding_functions

class TacticalMemory:
    def __init__(self):
        # Inicializar base de datos vectorial en disco (Nada de nube)
        self.client = chromadb.PersistentClient(path="./brain/memory_db")
        self.emb_fn = embedding_functions.DefaultEmbeddingFunction()
        self.collection = self.client.get_or_create_collection(
            name="incident_history", 
            embedding_function=self.emb_fn
        )

    def store_incident(self, incident_id, description, metadata):
        """Guarda un incidente para el futuro"""
        self.collection.add(
            documents=[description],
            metadatas=[metadata],
            ids=[incident_id]
        )
        print(f"[+] Memoria Táctica: Incidente {incident_id} guardado.")

    def compare_with_past(self, current_incident_desc):
        """Busca ataques similares en el pasado (Similitud del Coseno)"""
        results = self.collection.query(
            query_texts=[current_incident_desc],
            n_results=1
        )
        # Si la distancia es pequeña (ej. < 0.4), es el mismo patrón
        if results['distances'] and results['distances'][0][0] < 0.4:
            return {
                "match": True,
                "old_metadata": results['metadatas'][0][0],
                "confidence": 1 - results['distances'][0][0]
            }
        return {"match": False}
