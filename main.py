from agente import agente

print("== Agente de Estoque ==")
print("Digite 0 para sair")
while True:

    pergunta = input("Perguntar algo sobre o Estoque: ")

    if pergunta == "0":
        break

    resposta = agente(pergunta)

    print (resposta)