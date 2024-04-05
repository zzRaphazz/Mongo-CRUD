from database.vendedor.vendedorCreate import vendedorCreate
from database.connection import database
from bson.objectid import ObjectId

def vendedorCreateMenu():
    nome = str(input("Digite um nome: "))
    rg = str(input("Digite um rg: "))

    produtos = []
    execucao = True
    
    opcao = str(input("Deseja adicionar produtos? (s/n) "))
    if opcao == "s":
        while execucao:
            produtoID = str(input("Digite o id do produto: "))
            produtoID = ObjectId(produtoID)
            produtoCompleto = database.produto.find_one({"_id": produtoID})
            if produtoCompleto == None:
                print()
                print("Produto não encontrado!")
                print()
                return
            else:
                produtoNome = produtoCompleto["nome"]
                produtoDescricao = produtoCompleto["descricao"]
                produtoPreco = produtoCompleto["preco"]
            produto = {
                "id": produtoID,
                "nome": produtoNome,
                "descricao": produtoDescricao,
                "preco": produtoPreco
            }
            produtos.append(produto)

            opcao = str(input("deseja adicionar mais? (s/n) "))
            if opcao != "s":
                execucao = False

    vendedor = {
        "nome": nome.lower(),
        "rg": rg.lower(),
        "produtos": produtos
    }

    vendedorCreate(vendedor)