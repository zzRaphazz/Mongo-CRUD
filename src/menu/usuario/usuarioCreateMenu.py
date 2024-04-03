from database.usuarios.usuarioCreate import usuarioCreate

def usuarioCreateMenu():
    nome = str(input("Digite um nome: "))
    endereco = str(input("Digite um endereço: "))
    rg = str(input("Digite um rg: "))

    if nome == "":
        print()
        print("Nome não pode ser vazio!")
        input()
        return

    usuarioCreate(
        nome.lower(), endereco.lower(), rg.lower()
    )
    