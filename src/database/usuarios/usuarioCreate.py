from database.connection import database

def usuarioCreate(usuario):
    global database

    try:
        database.usuario.insert_one(usuario)
        print()
        print("Usuario registrado com sucesso!")
        input()
    except:
        print()
        print("! ERRO NA INSERÇÃO DE USUARIO !")
        input()
