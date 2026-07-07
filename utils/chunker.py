from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP

def criar_chunks(documentos):
    print("Criando chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP)
    chunks = splitter.split_documents(documentos)

    print(f'Total de chunks criados: {len(chunks)}')
    return chunks