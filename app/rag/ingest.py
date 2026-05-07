from sentence_transformers import SentenceTransformer
from app.rag.chroma_client import collection
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

KNOWLEDGE_PATH = "app/rag/knowledge"

documents = []
ids = []

for idx, filename in enumerate(os.listdir(KNOWLEDGE_PATH)):
    path = os.path.join(KNOWLEDGE_PATH, filename)

    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

        documents.append(text)
        ids.append(str(idx))

embeddings = model.encode(documents).tolist()

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids
)

print("Knowledge ingested successfully")