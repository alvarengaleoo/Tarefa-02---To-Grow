from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DOCUMENTS_PATH = BASE_DIR / "documentos"

QDRANT_PATH = BASE_DIR / "db"

QDRANT_LOCATION = str(QDRANT_PATH)

COLLECTION_NAME = "documentos"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

TOP_K = 3