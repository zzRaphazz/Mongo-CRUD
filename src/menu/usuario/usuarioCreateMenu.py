from database.usuario.usuarioCreate import usuarioCreate

def usuarioCreateMenu():
    nome = str(input("Digite um nome: "))

    if nome == "":
        print()
        print("Nome inválido!")
        input()
        return

    endereco = str(input("Digite um endereço: "))
    rg = str(input("Digite um rg: "))

    usuario = {
        "nome": nome.lower(),
        "endereco": endereco.lower(),
        "rg": rg.lower()
    }

    usuarioCreate(usuario)
    