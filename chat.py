import os
from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from config import COLLECTION_NAME, QDRANT_LOCATION, TOP_K
from utils.embeddings import criar_embeddings
from prompts.prompt import criar_prompt
from groq import Groq

#carrega as variaveis do .env
load_dotenv()

#cria o cliente da Groq utilizando a chave de api
client = Groq(
    api_key=os.getenv("GROQ_API_KEY"))

#carrega o mesmo modelo de embeddings utilizado na criação do banco
embeddings = criar_embeddings()

#abre a coleção já existente no banco
vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    path=QDRANT_LOCATION,
    collection_name=COLLECTION_NAME)

def perguntar(pergunta):
    """Busca informações no banco vetorial e envia para groq"""

    #busca os trechos mais parecidos com a pergunta
    documentos = vector_store.similarity_search(
        pergunta,
        k=TOP_K)
    
    #junta os trechos encontrados em um unico contexto
    contexto = "\n\n".join(
        documento.page_content
        for documento in documentos)
    
    #cria o prompt que sera enviado para a ia
    prompt = criar_prompt(contexto, pergunta)

    #envia a pergunta para a llm
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
    print("\nResposta: \n")
    print(resposta)    

