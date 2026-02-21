import chromadb

class VectorDB:
    def __init__(self, persist_directory="./chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_or_create_collection("calendar_data")

    def upsert_meeting(self, meeting_id, text_content, metadata):
        self.collection.add(
            ids=[meeting_id],
            documents=[text_content],
            metadatas=[metadata]
        )

    def search(self, query_text, top_k=3):
        results = self.collection.query(query_texts=[query_text], n_results=top_k)
        return results['documents'][0]