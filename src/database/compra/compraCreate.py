from database.connection import database

def compraCreate(compra):
    global database

    try:
        database.compra.insert_one(compra)
        print()
        print("Compra registrada com sucesso!")
        input()
    except:
        print()
        print("! ERRO NA INSERÇÃO DE COMPRA !")
        input()