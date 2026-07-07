from utils.loaders import carregar_documentos
from utils.chunker import criar_chunks

documentos = carregar_documentos()

chunks = criar_chunks(documentos)

print()

print(chunks[0].page_content)

