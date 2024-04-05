from database.connection import database

def compraUpdate(filtro, novoUsuario):
    global database

    try:
        database.compra.update_one(filtro, { "$set": novoUsuario })
        print()
        print("Compra atualizado com sucesso!")
        input()
    except:
        print()
        print("! ERRO NA ATUALIZAÇÃO DE COMPRA !")
        input()