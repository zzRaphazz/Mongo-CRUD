from database.usuario.usuarioUpdate import usuarioUpdate
from database.connection import database
from bson.objectid import ObjectId

def usuarioUpdateMenu():
    global database

    id = input("ID do usuario: ")

    if id == "":
        print()
        print("ID não pode ser vazio!")
        input()
        return

    filtro = {
        "_id": ObjectId(id)
    }

    usuario = database.usuario.find_one(filtro)

    if usuario == None:
        print("Usuario não encontrado")
        return

    print()
    print(f"- Você esta alterando o usuario {usuario['nome']} -")
    print("Deixe em branco para manter o mesmo valor")
    print()

    nome = input("Digite o novo nome: ")
    if nome == "":
        nome = usuario["nome"]

    endereco = input("Digite o novo endereço: ")
    if endereco == "":
        endereco = usuario["endereco"]

    rg = input("Digite o novo RG: ")
    if rg == "":
        rg = usuario["rg"]

    novoUsuario = {
        "nome": nome.lower(),
        "rg": rg.lower(),
        "endereco": endereco.lower()
    }

    usuarioUpdate(filtro, novoUsuario)
