import datetime
from bson.objectid import ObjectId
from database.connection import database
from database.compra.compraCreate import compraCreate

def compraCreateMenu():

    # Usuario
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

    # Produtos
    produtos = []
    execucao = True
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
            produtoVendedor = produtoCompleto["vendedor"]
            produtoDescricao = produtoCompleto["descricao"]
            produtoPreco = produtoCompleto["preco"]
        produto = {
            "_id": produtoID,
            "nome": produtoNome,
            "descricao": produtoDescricao,
            "preco": produtoPreco
        }
        produtos.append(produto)
        
        opcao = str(input("deseja adicionar mais? (s/n) "))
        if opcao != "s":
            execucao = False
    
    # Data
    data_compra = str(input("Digite a data da compra: (dd/mm/aaaa) "))
    data_compra = data_compra.lower().split("/")
    try:
        data_compra = datetime.datetime(int(data_compra[2]), int(data_compra[1]), int(data_compra[0]))
    except:
        print()
        print("Data inválida!")
        input()
        return
    
    # Valor 

    valorTotal = 0

    for produto in produtos:
        valorTotal += produto["preco"]

    compra ={
        "usuario": usuario,
        "produto": produtos,
        "data_compra": data_compra,
        "valorTotal": valorTotal
    }

    compraCreate(compra)
