from database.connection import database
from database.produtos.produtoCreate import produtoCreate
from bson.objectid import ObjectId

def produtosCreateMenu():
    nome = str(input("Digite um nome: "))
    descricao = str(input("Digite uma descrição: "))

    vendedorID = str(input("Digite o id do vendedor: "))
    # id = ObjectId(vendedorID)
    id = ObjectId("65e88681e8b9c289ed769491")

    vendedor = database.vendedor.find_one({"_id": id})
    if vendedor == None:
        print()
        print("Vendedor não encontrado!")
        input()
        return
    else:
        vendedorNome = vendedor["nome"]

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
        "vendedor": {
            "_id": id,
            "nome": vendedorNome
        },
        "descricao": descricao.lower(),
        "preco": preco,
        "estoque": estoque,
    }

    produtoCreate(produto)
