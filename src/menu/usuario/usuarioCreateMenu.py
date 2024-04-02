from database.usuarios.usuarioCreate import createUsuario

def usuarioCreateMenu():
    nome = str(input("Digite um nome: "))
    endereco = str(input("Digite um endereço: "))
    rg = str(input("Digite um rg: "))

    createUsuario(nome, endereco, rg)
    