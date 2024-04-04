from database.usuario.usuarioCreate import usuarioCreate

def usuarioCreateMenu():
    nome = str(input("Digite um nome: "))
    endereco = str(input("Digite um endereço: "))
    rg = str(input("Digite um rg: "))

    if nome == "":
        print()
        print("Nome não pode ser vazio!")
        input()
        return

    usuario = {
        "nome": nome.lower(),
        "endereco": endereco.lower(),
        "rg": rg.lower()
    }

    usuarioCreate(usuario)
    