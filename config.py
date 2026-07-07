from pathlib import Path

#caminhos do projeto
BASE_DIR = Path(__file__).resolve().parent
DOCUMENTS_PATH = BASE_DIR / "documentos"
QDRANT_PATH = BASE_DIR / "db"
QDRANT_LOCATION = str(QDRANT_PATH)

#configuração do banco vetorial
COLLECTION_NAME = "documentos"

#modelo utilizado para o embeddings
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

#configuração dos chunks
CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

# qtd de documentos retornados na busca
TOP_K = 3