from ferramentas import *
from llm import *
    
def formatar_resposta(ferramenta, resultado):

    if ferramenta == "todos produtos":
        texto = "Produtos cadastrados no estoque:\n\n"

        for produto in resultado:
            texto += f"- {produto}\n"

        return texto

    if ferramenta == "baixo estoque":
        if resultado.empty:
            return "Não existem produtos com estoque baixo."

        texto = "Produtos com estoque baixo:\n\n"

        for indice, linha in resultado.iterrows():
            texto += f"- {linha['Produto']} ({linha['Quantidade']} unidades)\n"

        return texto

    return None

def agente(pergunta):

    ferramentas = {
        "baixo estoque": baixo_estoque,
        "valor total": preco_total,
        "produto caro": produto_caro,
        "mais produto": mais_produto,
        "todos produtos": produtos,
        "produto barato": produto_barato,
    }

    descricoes = {
        "baixo estoque": "listar produtos com baixo estoque",
        "valor total": "informar valor total do estoque",
        "produto caro": "informar produto mais caro",
        "produto barato": "informar produto mais barato",
        "mais produto": "informar produto com maior quantidade",
        "todos produtos": "listar todos os produtos"
    }

    ferramenta = escolher_ferramenta(pergunta)
    ferramenta = ferramenta.strip().lower()

    resultado = ferramentas[ferramenta](dados)

    resposta_direta = formatar_resposta(
        ferramenta,
        resultado
    )

    if resposta_direta:
        return resposta_direta

    descricao = descricoes[ferramenta]

    resposta_final = Gera_resposta(
        pergunta,
        descricao,
        resultado
    )

    return resposta_final

ferramenta = escolher_ferramenta(
    " "
)

