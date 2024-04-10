from database.connection import database

def usuarioRead(filter):
    global database
    usuario = []

    for user in database.usuario.find(filter):
        usuario.append(user)

    print()
    if usuario == []:
        print("Nenhum usuario com esse filtro encontrado!")
        input()
    else:
        for user in usuario:
            print("_id:", user["_id"])
            print("nome:", user["nome"])
            print("endereco:", user["endereco"])
            print("rg:", user["rg"])
            input()

def usuarioReadAll():
    global database
    usuario = []

    for user in database.usuario.find():
        usuario.append(user)

    print()
    if usuario == []:
        print("Nenhum usuario encontrado no sistema!")
        input()
    else:
        for user in usuario:
            print("ID:", user["_id"])
            print("Nome:", user["nome"])
            print("Endereço:", user["endereco"])
            print("RG:", user["rg"])
            input()
