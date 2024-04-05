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
            print("ID:", buy["_id"])
            print("Data:", buy["data"])
            print("Valor:", buy["valor"])
            print("Usuario: ")
            usuarioRead({"_id": buy["usuario"]})
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
            print("ID:", buy["_id"])
            print("Data:", buy["data_compra"])
            print("Valor:", buy["valor_total"])
            print("Usuario: ")
            print("     " + "ID:", buy["usuario"]["_id"])
            print("     " + "Nome:", buy["usuario"]["nome"])
            print("     " + "Endereço:", buy["usuario"]["endereco"])
            print("Produtos: ")
            for produto in buy["produto"]:
                print("     " + "ID:", produto["_id"])
                print("     " + "Nome:", produto["nome"])
                print("     " + "Vendedor:")
                print("         " + "ID:", produto["vendedor"]["_id"])
                print("         " + "Nome:", produto["vendedor"]["nome"])
                print("     " + "Descrição:", produto["descricao"])
                print("     " + "Preço:", produto["preco"])
                print()
            input()