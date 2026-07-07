import os
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from config import COLLECTION_NAME, QDRANT_LOCATION, TOP_K
from utils.embeddings import criar_embeddings
from prompts.prompt import criar_prompt
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"))

embeddings = criar_embeddings()

vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    path=QDRANT_LOCATION,
    collection_name=COLLECTION_NAME)

def perguntar(pergunta):
    documentos = vector_store.similarity_search(
        pergunta,
        k=TOP_K)
    
    contexto = "\n\n".join(
        documento.page_content
        for documento in documentos)
    
    prompt = criar_prompt(contexto, pergunta)

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    return resposta.choices[0].message.content

if __name__ == "__main__":
    pergunta = input("Digite sua pergunta: ")
    resposta = perguntar(pergunta)
    print("\nresposta: \n")
    print(resposta)    

