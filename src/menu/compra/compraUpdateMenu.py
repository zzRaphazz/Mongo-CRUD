from database.compra.compraUpdate import compraUpdate
from database.connection import database
from bson.objectid import ObjectId
from menu.crdProdutosMenu import crdProdutosMenu
import datetime

def compraUpdateMenu():
    global database

    id = input("ID da compra: ")
    if id == "":
        print()
        print("ID não pode ser vazio!")
        input()
        return
    
    filtro = {
        "_id": ObjectId(id)
    }

    compra = database.compra.find_one(filtro)
    if compra == None:
        print()
        print("Compra não encontrada")
        input()
        return
    
    print()
    print(f"- Você esta alterando a compra -")
    print("Deixe em branco para manter o mesmo valor")
    print()

    opcao = str(input("Deseja alterar o usuario? (s/n) "))
    if opcao == "s":
        usuarioID = str(input("Digite o id do usuario: "))
        usuarioID = ObjectId(usuarioID)
        usuarioCompleto = database.usuario.find_one({"_id": usuarioID})
        if usuarioCompleto == None:
            print()
            print("Usuario não encontrado!")
            print()
            return
        else:
            usuarioNome = usuarioCompleto["nome"]
            usuarioEndereco = usuarioCompleto["endereco"]
        usuario = {
            "_id": usuarioID,
            "nome": usuarioNome.lower(),
            "endereco": usuarioEndereco.lower()
        }
    else:
        usuario = compra["usuario"]

    opcao = str(input("Deseja alterar os produtos? (s/n) "))
    if opcao == "s":
        produtos = crdProdutosMenu(compra["produto"])
    else:
        produtos = compra["produto"]

    data_compra = str(input("Digite a data da compra: (dd/mm/aaaa) "))
    if data_compra == "":
        data_compra = compra["data_compra"]
    else:
        data_compra = data_compra.lower().split("/")
        data_compra = datetime.datetime(int(data_compra[2]), int(data_compra[1]), int(data_compra[0]))
    
    valorTotal = 0
    for produto in produtos:
        valorTotal += produto["preco"]
    
    compra = {
        "usuario": usuario,
        "produto": produtos,
        "data_compra": data_compra,
        "valorTotal": valorTotal
    }

    compraUpdate(filtro, compra)
