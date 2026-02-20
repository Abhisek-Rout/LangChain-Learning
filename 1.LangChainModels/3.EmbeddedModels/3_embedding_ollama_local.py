from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="embeddinggemma:latest",
)

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

vector = embeddings.embed_documents(documents)

vector_single = embeddings.embed_query(documents[0])

print(str(vector))

print(str(vector_single))

