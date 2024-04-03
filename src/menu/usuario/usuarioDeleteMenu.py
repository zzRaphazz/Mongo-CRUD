from database.usuarios.usuarioDelete import usuarioDelete

def usuarioDeleteMenu():
    filtro = {
        "nome": input("Digite o nome do usuario: ")
    }
    usuarioDelete(filtro)
    input()