from database.usuarios.usuarioCreate import usuarioCreate

def usuarioCreateMenu():
    nome = str(input("Digite um nome: "))
    endereco = str(input("Digite um endereço: "))
    rg = str(input("Digite um rg: "))

    usuarioCreate(nome, endereco, rg)
    