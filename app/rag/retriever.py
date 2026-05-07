from sentence_transformers import SentenceTransformer
from app.rag.chroma_client import collection

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_context(query, top_k=3):

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    documents = results["documents"][0] # type: ignore

    return "\n".join(documents)