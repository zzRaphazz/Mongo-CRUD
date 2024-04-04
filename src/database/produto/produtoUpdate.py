from database.connection import database

def produtoUpdate(filtro, novoProduto):
    global database
    
    try:
        database.produto.update_one(filtro, { "$set": novoProduto })
        print()
        print("Produto atualizado com sucesso!")
        input()
    except:
        print()
        print("! ERRO NA ATUALIZAÇÃO DE PRODUTO !")
        input()