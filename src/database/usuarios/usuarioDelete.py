from database.connection import database

def usuarioDelete(filtro):
    global database
    
    print()
    usuario = database.usuario.find_one(filtro)
    if usuario == None:
        print("Usuario não encontrado")
        return
    else:
        database.usuario.delete_one(filtro)
        print(f"Usuario {usuario['nome']} deletado")