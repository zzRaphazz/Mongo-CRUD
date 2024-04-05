from database.connection import database

def vendedorDelete(filtro):
    global database

    print()
    produto = database.vendedor.find_one(filtro)
    if produto == None:
        print("Vendedor não encontrado")
        return
    else:
        database.vendedor.delete_one(filtro)
        print(f"Vendedor {produto['nome']} deletado")
        input()
