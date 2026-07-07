from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL

def criar_embeddings():
    print("Carregando o modelo de embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return embeddings
