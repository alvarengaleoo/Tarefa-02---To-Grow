from utils.embeddings import criar_embeddings

embeddings = criar_embeddings()

vetor = embeddings.embed_query("Como solicitar férias?")

print(f"Tamanho do vetor: {len(vetor)}")
print(vetor[:10])