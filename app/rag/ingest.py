from sentence_transformers import SentenceTransformer
from app.rag.chroma_client import collection
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

KNOWLEDGE_PATH = "app/rag/knowledge"

documents = []
ids = []
metadatas = []

chunk_id = 0

for filename in os.listdir(KNOWLEDGE_PATH):

    path = os.path.join(KNOWLEDGE_PATH, filename)

    with open(path, "r", encoding="utf-8") as file:

        text = file.read()

        chunks = text.split("\n\n")

        for chunk in chunks:

            documents.append(chunk)

            ids.append(str(chunk_id))

            metadatas.append({
                "source": filename
            })

            chunk_id += 1

embeddings = model.encode(documents).tolist()

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids,
    metadatas=metadatas
)

print("Chunked knowledge ingestion completed")