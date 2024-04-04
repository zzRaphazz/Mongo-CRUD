from database.usuario.usuarioRead import usuarioRead, usuarioReadAll

def usuarioReadMenu():
    
    filtro = {
        "nome": str(input("Digite um nome: ")).lower()
    }

    if filtro["nome"] == "":
        usuarioReadAll()
    else:
        usuarioRead(filtro)
