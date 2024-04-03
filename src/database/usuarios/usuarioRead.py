from database.connection import database

def usuarioRead(filter):
    global database
    usuarios = []

    for user in database.usuario.find(filter):
        usuarios.append(user)

    print()
    if usuarios == []:
        print("Nenhum usuario com esse filtro encontrado!")
        input()
    else:
        for user in usuarios:
            print("ID:", user["_id"])
            print("Nome:", user["nome"])
            print("Endereço:", user["endereco"])
            print("RG:", user["rg"])
            input()

def usuarioReadAll():
    global database
    usuarios = []

    for user in database.usuario.find():
        usuarios.append(user)

    print()
    if usuarios == []:
        print("Nenhum usuario encontrado no sistema!")
        input()
    else:
        for user in usuarios:
            print("ID:", user["_id"])
            print("Nome:", user["nome"])
            print("Endereço:", user["endereco"])
            print("RG:", user["rg"])
            input()
