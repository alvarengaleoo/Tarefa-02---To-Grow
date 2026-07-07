# Sistema RAG com Qdrant e Groq

## Sobre o projeto

Projeto desenvolvido para estudar a técnica de RAG (Retrieval-Augmented Generation).

O sistema carrega documentos, gera embeddings, armazena os dados no Qdrant e utiliza a API da Groq para responder perguntas com base nos documentos.

---

## Tecnologias

- Python
- LangChain
- Qdrant
- Groq
- Hugging Face

---

## Estrutura

```
documentos/
prompts/
utils/

chat.py
config.py
criar_db.py
```

---

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie o banco vetorial:

```bash
python criar_db.py
```

Execute o chat:

```bash
python chat.py
```

---

## Fluxo

```
Documentos
   ↓
Embeddings
   ↓
Qdrant
   ↓
Groq
   ↓
Resposta
```