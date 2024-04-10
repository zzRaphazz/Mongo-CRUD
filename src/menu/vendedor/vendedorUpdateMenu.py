from database.vendedor.vendedorUpdate import vendedorUpdate
from database.connection import database
from bson.objectid import ObjectId
from menu.crdProdutosMenu import crdProdutosMenu
from function.recarregarProdutos import recarregarProdutos

def vendedorUpdateMenu():
    global database
    
    id = input("ID do vendedor: ")

    if id == "":
        print()
        print("ID não pode ser vazio!")
        input()
        return
    
    filtro = {
        "_id": ObjectId(id)
    }

    vendedor = database.vendedor.find_one(filtro)
    if vendedor == None:
        print()
        print("Vendedor não encontrado")
        input()
        return
    
    print()
    print(f"- Você esta alterando o vendedor {vendedor['nome']} -")
    print("Deixe em branco para manter o mesmo valor")
    print()

    nome = str(input("Digite um nome: "))
    if nome == "":
        nome = vendedor["nome"]
    
    rg = str(input("Digite um rg: "))
    if rg == "":
        rg = vendedor["rg"]

    opcao = str(input("Deseja alterar os produtos? (s/n) "))
    if opcao == "s":
        produtos = crdProdutosMenu(vendedor["produtos"])
    else:
        produtos = vendedor["produtos"]

    vendedor = {
        "nome": nome.lower(),
        "rg": rg.lower(),
        "produtos": produtos
    }

    vendedorUpdate(filtro, vendedor)

    vendedor = {
        "_id": ObjectId(id),
        "nome": nome.lower(),
        "rg": rg.lower(),
        "produtos": produtos
    }

    recarregarProdutos(vendedor)
    