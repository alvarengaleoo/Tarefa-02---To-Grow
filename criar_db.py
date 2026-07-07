from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

from config import COLLECTION_NAME, QDRANT_LOCATION
from utils.loaders import carregar_documentos
from utils.chunker import criar_chunks
from utils.embeddings import criar_embeddings

def criar_banco_vetorial():
    print("-" * 50)
    print("Criando o banco vetorial...")
    print("-" * 50)

    documentos = carregar_documentos()
    chunks = criar_chunks(documentos)
    embeddings = criar_embeddings()
    
    QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        path=QDRANT_LOCATION,
        collection_name=COLLECTION_NAME)
    
    print()
    print('Banco vetorial criado com sucesso...')

if __name__ == "__main__":
    criar_banco_vetorial()


