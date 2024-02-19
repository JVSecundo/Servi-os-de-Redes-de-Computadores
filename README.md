### Utilização de Variáveis de Ambiente em Docker

Este é um projeto simples que demonstra como utilizar variáveis de ambiente em uma aplicação Dockerizada.

## Pré-requisitos

- Docker instalado e configurado

## Descrição

O projeto consiste em uma aplicação Python básica que imprime o valor de uma variável de ambiente chamada `MY_VARIABLE`.

### Arquivos

- `app.py`: Script Python que lê e exibe o valor da variável de ambiente.
- `Dockerfile`: Arquivo Dockerfile para construir a imagem Docker.
- `README.md`: Este arquivo de documentação.

## Passo a Passo

Aqui está o passo a passo para executar cada parte da atividade:

### Atividade 1: Hello World Dockerfile

1. **Construir a imagem Docker a partir do Dockerfile:**
- docker build -t hello-world .

2. **Executar um contêiner a partir da imagem:**
- docker run hello-world
  
### Atividade 2: Aplicação Python Simples

1. **Construir a imagem Docker para a aplicação Python:**
- docker build -t python-app .

2. **Executar um contêiner a partir da imagem:**
- docker run python-app


### Atividade 3: Montagem de Volume

1. **Construir a imagem Docker para a montagem de volume:**
- docker build -t volume-example .


2. **Executar um contêiner e montar um arquivo dentro do diretório do contêiner:**
- docker run -v /caminho/para/arquivo/local:/app volume-example
  
3. **O contêiner foi iniciado com sucesso e você está agora dentro do terminal do contêiner, representado pelo prompt /app #.**
- Da o comando "ls", para ver o que tem dentro

### Atividade 4: Variáveis de Ambiente

1. **Construir a imagem Docker para a aplicação que utiliza variáveis de ambiente:**
- docker build -t env-example .


2. **Executar um contêiner fornecendo um valor diferente para a variável de ambiente:**
- docker run -e MY_VARIABLE=NovoValor env-example

