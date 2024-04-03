from database.usuarios.usuarioRead import readAllUser, readUser

def usuarioReadMenu():
    
    filtro = {
        "nome": str(input("Digite um nome: "))
    }

    if filtro["nome"] == "":
        readAllUser()
    else:
        readUser(filtro)
