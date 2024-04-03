from database.usuarios.usuarioUpdate import usuarioUpdate

def usuarioUpdateMenu():
    filtro = {
        "nome": str(input("Digite o nome do usuario: "))
    }

    usuarioUpdate(filtro)
