# Agente de Controle de Estoque com IA

### Sistema de Consulta Inteligente utilizando LLM + Ferramentas Python

<p align="center">
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Python-3.12+-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-purple?style=for-the-badge&logo=pandas"/>
</p>

---

## Sobre o Projeto

O **Agente de Controle de Estoque** é uma aplicação desenvolvida para demonstrar a integração entre **Modelos de Linguagem (LLMs)** e **ferramentas Python**, permitindo que usuários consultem informações de estoque utilizando linguagem natural.

O sistema utiliza um modelo local executado através do **Ollama** para interpretar perguntas, selecionar automaticamente a ferramenta adequada e gerar respostas amigáveis com base nos dados armazenados em uma planilha Excel.

O projeto foi desenvolvido com foco em aprendizado de conceitos de:

* Agentes de IA
* Seleção de Ferramentas (Tool Calling)
* Engenharia de Prompt
* Processamento de Dados com Pandas
* Integração de LLMs Locais

---

## Tecnologias Utilizadas

<p align="center">
  <img src="https://skillicons.dev/icons?i=python" />
</p>

* Python
* Ollama
* Llama 3.2
* Pandas
* OpenPyXL
* Excel (.xlsx)

---

## Funcionalidades

### Consulta por Linguagem Natural

O usuário pode realizar perguntas como:

* Qual o valor total do estoque?
* Qual o produto mais caro?
* Qual o produto mais barato?
* Qual produto possui a maior quantidade?
* Quais produtos estão com estoque baixo?
* Quais são todos os produtos cadastrados?

---

### Seleção Automática de Ferramentas

O LLM atua como um roteador inteligente e escolhe automaticamente qual função deve ser executada para responder a pergunta do usuário.

Ferramentas disponíveis:

* Baixo Estoque
* Valor Total
* Produto Mais Caro
* Produto Mais Barato
* Produto com Maior Quantidade
* Listagem Completa de Produtos

---

### Leitura de Planilha

Os dados são carregados diretamente de um arquivo Excel contendo:

* Nome do Produto
* Quantidade
* Preço Unitário

---

### Arquitetura Modular

O projeto foi organizado em múltiplos arquivos para facilitar manutenção e expansão:

* main.py
* agente.py
* ferramentas.py
* prompts.py
* estoque.xlsx

---

## Fluxo do Agente

1. O usuário faz uma pergunta.
2. O LLM analisa a intenção da pergunta.
3. O LLM escolhe a ferramenta correta.
4. A ferramenta consulta os dados do estoque.
5. O resultado é retornado ao modelo.
6. O modelo gera uma resposta amigável ao usuário.

---

## Como rodar o projeto em localhost

### Pré-requisitos

* Python 3.12+
* Ollama instalado

### Instalar dependências

```bash
pip install -r requirements.txt
```

### Baixar o modelo utilizado

```bash
ollama pull llama3.2
```

### Iniciar o Ollama

```bash
ollama serve
```

### Executar o projeto

```bash
python main.py
```

---

## Exemplo de Uso

```text
Perguntar algo sobre o estoque:
Qual o produto mais caro?

Resposta:
O produto mais caro do estoque é Mesa.
```

```text
Perguntar algo sobre o estoque:
Quais produtos estão com estoque baixo?

Resposta:
Produtos com estoque baixo:

- Webcam (3 unidades)
- Microfone (2 unidades)
```

---

## Aprendizados do Projeto

Durante o desenvolvimento foram explorados conceitos importantes de agentes baseados em LLMs:

* Prompt Engineering
* Tool Calling
* Roteamento de Ferramentas
* Integração entre IA e código Python
* Tratamento de respostas de modelos locais
* Estruturação modular de projetos

---

## Melhorias Futuras

* Histórico de conversas
* Memória entre interações
* Inclusão de novas ferramentas
* Interface Web com Streamlit
* Integração com banco de dados
* Utilização de Function Calling nativo
* Deploy em nuvem

---

## Licença

Este projeto foi desenvolvido para fins de estudo, aprendizado e demonstração de conhecimentos em Inteligência Artificial e Engenharia de Software.

---
