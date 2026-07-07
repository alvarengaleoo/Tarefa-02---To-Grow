def criar_prompt(contexto, pergunta):
    """Monta o prompt que sera enviado para a IA."""

    prompt = f"""
Você é um assistente de IA.

Responda apenas utilizando as informações presentes no contexto abaixo.

Se a resposta não estiver no contexto, informe que a resposta nao foi encontrada nos documentos.

Contexto:

{contexto}

Pergunta:

{pergunta}

Resposta:
"""

    return prompt