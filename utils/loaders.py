from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from config import DOCUMENTS_PATH

def carregar_documentos():
    print("Carregando documentos...")

    documentos = []

    for arquivo in DOCUMENTS_PATH.glob("*.pdf"):
        loader = PyPDFLoader(str(arquivo))
        documentos.extend(loader.load())

    for arquivo in DOCUMENTS_PATH.glob("*.docx"):
        loader = Docx2txtLoader(str(arquivo))
        documentos.extend(loader.load())
    
    for arquivo in DOCUMENTS_PATH.glob("*.txt"):
        loader = TextLoader(str(arquivo), encoding="utf-8")
        documentos.extend(loader.load())

    print(f'Total de documentos carregados: {len(documentos)}')

    return documentos