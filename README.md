<div align="center">

# Projeto CRUD com MongoDB e Python

![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

</div>

Este projeto é a segunda atividade prática da disciplina de Bancos de Dados não Relacional, com o intuito de aprofundar conhecimentos e habilidades no uso do MongoDB, um sistema de gerenciamento de banco de dados orientado a documentos, em conjunto com a linguagem de programação Python. O projeto visa desenvolver e demonstrar operações fundamentais de CRUD (Create, Read, Update, Delete), aplicadas em um contexto real de aplicação.

## 🎯 Objetivos:

- **Entender a Estrutura do MongoDB:** Aprender como os dados são estruturados em coleções e documentos no MongoDB, e como essa flexibilidade pode ser utilizada para construir aplicações robustas.
- **Realizar Operações de CRUD:** Desenvolver habilidades práticas ao implementar as operações básicas de um banco de dados: criar, ler, atualizar e deletar documentos no MongoDB utilizando Python.
- **Explorar Python no Contexto de Dados:** Utilizar a linguagem Python para interagir com o MongoDB, empregando bibliotecas específicas que facilitam a manipulação de dados.
- **Construir uma Aplicação Prática:** Integrar os conhecimentos adquiridos para desenvolver uma aplicação que realiza todas as operações de CRUD, proporcionando uma experiência de aprendizado completa.

## 🖥️ Requisitos

Para executar este projeto, você precisará de:

- Python 3.6 ou superior instalado em seu sistema.
- Acesso ao MongoDB, que pode ser uma instância local ou em nuvem (MongoDB Atlas).
- Biblioteca pymongo instalada, que pode ser feita através do comando

        pip install pymongo

## ⚙️ Configuração e Execução

### Configuração do Ambiente

1. **Instalação do MongoDB:** Certifique-se de que o MongoDB esteja instalado e configurado corretamente em sua máquina. Caso prefira utilizar o MongoDB Atlas, crie uma conta e configure seu cluster seguindo as instruções fornecidas na plataforma.

2. **Configuração do Python e Dependências:** Abra o terminal e execute o seguinte comando para instalar a biblioteca necessária:

        pip install pymongo

3. **Coloque sua senha do banco:** Abra o arquivo [connection.py](src/database/connection.py), e mude o campo password para a senha do root.

### Como Executar:

1. Clone o Repositório:

        git clone https://github.com/felipe-sant/atv2-bd3.git

2. Edite o arquivo de configuração com as credenciais do seu banco de dados MongoDB.

3. Navegue até a pasta do projeto clonado e execute o script principal utilizando o Python:

        python src/main.py

