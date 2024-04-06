from database.connection import database

def vendedorUpdate(filtro, novoVendedor):
    global database

    try:
        database.vendedor.update_one(filtro, { "$set": novoVendedor })
        print()
        print("Vendedor atualizado com sucesso!")
        input()
    except:
        print()
        print("! ERRO NA ATUALIZAÇÃO DE VENDEDOR !")
        input()