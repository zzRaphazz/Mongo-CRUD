from database.connection import database
from database.produto.produtoCreate import produtoCreate
from bson.objectid import ObjectId

def produtoCreateMenu():
    nome = str(input("Digite um nome: "))
    if nome == "":
        print()
        print("Nome inválido!")
        input()
        return

    descricao = str(input("Digite uma descrição: "))

    try:
        preco = float(input("Digite um preço: "))
    except:
        print()
        print("Preço inválido!")
        input()
        return
    
    try:
        estoque = int(input("Digite o estoque: "))
    except:
        print()
        print("Estoque inválido!")
        input()
        return

    produto = {
        "nome": nome.lower(),
        "vendedor": {},
        "descricao": descricao.lower(),
        "preco": preco,
        "estoque": estoque,
    }

    produtoCreate(produto)
