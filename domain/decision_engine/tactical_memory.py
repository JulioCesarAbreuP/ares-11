
import chromadb
from chromadb.utils import embedding_functions
from core.events import EventBus
from core.utils import log_event, trace, retry, sanitize_input

class TacticalMemory:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./brain/memory_db")
        self.emb_fn = embedding_functions.DefaultEmbeddingFunction()
        self.collection = self.client.get_or_create_collection(
            name="incident_history", 
            embedding_function=self.emb_fn
        )

    @trace(stage="tactical_memory")
    @retry(retries=2, delay=1.0)
    def store_incident(self, incident_id, description, metadata):
        incident_id = sanitize_input(incident_id)
        description = sanitize_input(description)
        metadata = sanitize_input(metadata)
        self.collection.add(
            documents=[description],
            metadatas=[metadata],
            ids=[incident_id]
        )
        log_event("memory.incident_stored", {"id": incident_id, "metadata": metadata}, context={"stage": "tactical_memory"})
        print(f"[+] Memoria Táctica: Incidente {incident_id} guardado.")
        EventBus().publish("memory.incident_stored", {"id": incident_id, "metadata": metadata})

    @trace(stage="tactical_memory")
    @retry(retries=2, delay=1.0)
    def compare_with_past(self, current_incident_desc):
        current_incident_desc = sanitize_input(current_incident_desc)
        results = self.collection.query(
            query_texts=[current_incident_desc],
            n_results=1
        )
        if results['distances'] and results['distances'][0][0] < 0.4:
            log_event("memory.incident_match", {"confidence": 1 - results['distances'][0][0], "old_metadata": results['metadatas'][0][0]}, context={"stage": "tactical_memory"})
            return {
                "match": True,
                "old_metadata": results['metadatas'][0][0],
                "confidence": 1 - results['distances'][0][0]
            }
        log_event("memory.no_match", {"desc": current_incident_desc}, context={"stage": "tactical_memory"})
        return {"match": False}