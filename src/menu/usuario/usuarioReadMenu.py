from database.usuarios.usuarioRead import usuarioRead, usuarioReadAll

def usuarioReadMenu():
    
    filtro = {
        "nome": str(input("Digite um nome: "))
    }

    if filtro["nome"] == "":
        usuarioReadAll()
    else:
        usuarioRead(filtro)
