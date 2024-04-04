from database.usuario.usuarioUpdate import usuarioUpdate

def usuarioUpdateMenu():
    filtro = {
        "nome": str(input("Digite o nome do usuario: ")).lower()
    }

    if filtro["nome"] == "":
        print()
        print("Nome não pode ser vazio!")
        input()
        return

    usuarioUpdate(filtro)
