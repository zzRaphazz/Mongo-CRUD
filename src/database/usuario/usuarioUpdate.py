from database.connection import database

def usuarioUpdate(filtro, novoUsuario):
    global database

    try:
        database.usuario.update_one(filtro, { "$set": novoUsuario })
        print()
        print("Usuario atualizado com sucesso!")
        input()
    except:
        print()
        print("! ERRO NA ATUALIZAÇÃO DE USUARIO !")
        input()