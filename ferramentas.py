import pandas as pd

def ler_estoque():
    return pd.read_excel("estoque.xlsx")

dados = ler_estoque()

def baixo_estoque(dados):
    estoqueBaixo = dados[dados["Quantidade"] < 5]
    return estoqueBaixo

def produtos(dados):
    lista_produtos = dados["Produto"].tolist()
    return lista_produtos

def preco_total(dados):
    valortotal = 0
    for indice, linha in dados.iterrows():
        valortotal += linha["Quantidade"]*linha["preço Unidade"]         
    return valortotal

def produto_caro(dados):
    maior = 0
    item = 0
    for indice, linha in dados.iterrows():
        if linha["preço Unidade"] > maior:
            maior = linha["preço Unidade"]
            item = linha["Produto"]
        
    return item

def produto_barato(dados):
    menor = float('inf')
    item = 0
    for indice, linha in dados.iterrows():
        if linha["preço Unidade"] < menor:
            menor = linha["preço Unidade"]
            item = linha["Produto"]
        
    return item

def mais_produto(dados):
    maior = 0
    item = 0
    for indice, linha in dados.iterrows():
        if linha["Quantidade"] > maior:
            maior = linha["Quantidade"]
            item = linha["Produto"]
        
    return item   