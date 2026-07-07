def criar_prompt(contexto, pergunta):

    prompt = f"""
Você é um assistente de IA.

Responda apenas utilizando as informações presentes no contexto abaixo.

Se a resposta não estiver no contexto, diga que ela não foi encontrada.

Contexto:

{contexto}

Pergunta:

{pergunta}

Resposta:
"""

    return prompt