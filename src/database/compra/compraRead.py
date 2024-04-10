from database.connection import database
from database.usuario.usuarioRead import usuarioRead

def compraRead(filter):
    global database
    compra = []

    for buy in database.compra.find(filter):
        compra.append(buy)

    print()
    if compra == []:
        print("Nenhuma compra com esse filtro encontrado!")
        input()
    else:
        for buy in compra:
            print("_id:", buy["_id"])
            print("usuario: ")
            print("     " + "_id:", buy["usuario"]["_id"])
            print("     " + "nome:", buy["usuario"]["nome"])
            print("     " + "endereco:", buy["usuario"]["endereco"])
            print("produto: ")
            for produto in buy["produto"]:
                print("     " + "_id:", produto["_id"])
                print("     " + "nome:", produto["nome"])
                print("     " + "descricao:", produto["descricao"])
                print("     " + "preco:", produto["preco"])
                print("--------------------")
            print("data_compra:", buy["data_compra"])
            print("valorTotal:", buy["valorTotal"])
            input()

def compraReadAll():
    global database
    compra = []

    for buy in database.compra.find():
        compra.append(buy)

    print()
    if compra == []:
        print("Nenhuma compra encontrada no sistema!")
        input()
    else:
        for buy in compra:
            print("_id:", buy["_id"])
            print("usuario: ")
            print("     " + "_id:", buy["usuario"]["_id"])
            print("     " + "nome:", buy["usuario"]["nome"])
            print("     " + "endereco:", buy["usuario"]["endereco"])
            print("produto: ")
            for produto in buy["produto"]:
                print("     " + "_id:", produto["_id"])
                print("     " + "nome:", produto["nome"])
                print("     " + "descricao:", produto["descricao"])
                print("     " + "preco:", produto["preco"])
                print("     " + "--------------------")
            print("data_compra:", buy["data_compra"])
            print("valorTotal:", buy["valorTotal"])
            input()