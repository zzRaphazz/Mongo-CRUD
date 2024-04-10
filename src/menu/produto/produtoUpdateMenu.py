from database.produto.produtoUpdate import produtoUpdate
from database.connection import database
from bson.objectid import ObjectId

def produtoUpdateMenu():
    global database

    id = input("ID do produto: ")

    if id == "":
        print()
        print("ID não pode ser vazio!")
        input()
        return

    filtro = {
        "_id": ObjectId(id)
    }
    
    produto = database.produto.find_one(filtro)

    if produto == None:
        print("Produto não encontrado")
        return
    
    print()
    print(f"- Você esta alterando o produto {produto['nome']} -")
    print("Deixe em branco para manter o mesmo valor")
    print()

    nome = input("Digite o novo nome: ")
    if nome == "":
        nome = produto["nome"]

    descricao = input("Digite a nova descrição: ")
    if descricao == "":
        descricao = produto["descricao"]

    try:
        preco = float(input("Digite o novo preço: "))
    except:
        preco = produto["preco"]

    try:
        estoque = int(input("Digite o novo estoque: "))
    except:
        estoque = produto["estoque"]

    novoProduto = {
        "nome": nome.lower(),
        "descricao": descricao.lower(),
        "preco": preco,
        "estoque": estoque,
    }

    produtoUpdate(filtro, novoProduto)