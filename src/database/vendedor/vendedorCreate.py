from database.connection import database

def vendedorCreate(produto):
    global database

    try: 
        database.vendedor.insert_one(produto)
        print()
        print("Vendedor registrado com sucesso!")
        input()
    except:
        print()
        print("! ERRO NA INSERÇÃO DE VENDEDOR !")
        input()