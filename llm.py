from ollama import chat

def escolher_ferramenta(pergunta):
    
    prompt = f"""

    Você é um seletor de ferramentas e possui 6 ferramentas:

    - baixo estoque 
    - valor total 
    - produto caro 
    - mais produto 
    - todos produtos 
    - produto barato

    Pergunta do usuário:
    {pergunta}

    IMPORTANTE:
    Você deve responder SOMENTE com UMA destas opções:

    baixo estoque
    valor total
    produto caro
    mais produto
    todos produtos
    produto barato

    Não explique.
    Não escreva frases.
    Não escreva pontuação.
    """
    resposta = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return resposta ["message"]["content"]

def Gera_resposta(pergunta, descricoes, resultado):
    prompt = f"""
    
    Você é um assistente de controle de estoque

    PERGUNTA DO USUÁRIO:
    {pergunta}

    DESCRIÇÃO DA FERRAMENTA:
    {descricoes}

    RESULTADO OFICIAL DA FERRAMENTA:
    {resultado}

    Responda ao usuario de forma simples e clara usando essas informações.
    
    REGRAS OBRIGATÓRIAS:

    1. O RESULTADO OFICIAL está correto.
    2. Você NÃO pode alterar o resultado.
    3. Você NÃO pode inventar produtos.
    4. Você NÃO pode fazer cálculos.
    5. Você NÃO pode usar conhecimento externo.
    6. Você NÃO pode substituir palavras do resultado.
    7. Sua única função é transformar o resultado em uma frase amigável.

    EXEMPLOS:

    Pergunta:
    Qual o produto mais caro?

    Resultado Oficial:
    Mesa

    Resposta:
    O produto mais caro do estoque é Mesa.

    Pergunta:
    Qual o valor total do estoque?

    Resultado Oficial:
    4500

    Resposta:
    O valor total do estoque é R$ 4500.

    Agora responda ao usuário usando EXATAMENTE o resultado oficial fornecido.
    """

    resposta = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return resposta["message"]["content"]