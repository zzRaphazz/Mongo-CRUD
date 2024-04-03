from database.usuarios.usuarioDelete import usuarioDelete

def usuarioDeleteMenu():
    filtro = {
        "nome": input("Digite o nome do usuario: ").lower()
    }

    if filtro["nome"] == "":
        print()
        print("Nome não pode ser vazio!")
        input()
        return

    usuarioDelete(filtro)
    input()