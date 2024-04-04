from database.connection import database

def produtoCreate(produto):
    global database

    try:
        database.produtos.insert_one(produto)
        print()
        print("Produto registrado com sucesso!")
        input()
    except:
        print()
        print("! ERRO NA INSERÇÃO DE PRODUTO !")
        input()
