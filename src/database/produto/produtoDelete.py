from database.connection import database

def produtoDelete(filtro):
    global database
    
    print()
    produto = database.produto.find_one(filtro)
    if produto == None:
        print("Produto não encontrado")
        return
    else:
        database.produto.delete_one(filtro)
        print(f"Produto {produto['nome']} deletado")