from langchain_huggingface import HuggingFaceEmbeddings
from config import EMBEDDING_MODEL

def criar_embeddings():
    """Carrega o modelo utilizado para gerar os embeddings."""

    print("Carregando o modelo de embeddings...")

    #inicializa o modelo de embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    return embeddings
