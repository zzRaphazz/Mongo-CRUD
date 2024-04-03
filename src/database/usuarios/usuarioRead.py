from database.connection import database

def readUser(filter):
    global database
    usuarios = []

    for user in database.usuario.find(filter):
        usuarios.append(user)

    if usuarios == []:
        print()
        print("Nenhum usuario com esse filtro encontrado!")
    else:
        for user in usuarios:
            print()
            print("ID:", user["_id"])
            print("Nome:", user["nome"])
            print("Endereço:", user["endereco"])
            print("RG:", user["rg"])
            input()

def readAllUser():
    global database
    usuarios = []

    for user in database.usuario.find():
        usuarios.append(user)

    if usuarios == []:
        print()
        print("Nenhum usuario encontrado no sistema!")
    else:
        for user in usuarios:
            print()
            print("ID:", user["_id"])
            print("Nome:", user["nome"])
            print("Endereço:", user["endereco"])
            print("RG:", user["rg"])
            input()
