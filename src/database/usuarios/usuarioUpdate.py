from database.connection import database

def usuarioUpdate(filtro):
    global database
    usuario = database.usuario.find_one(filtro)

    print()
    if usuario == None:
        print("Usuario não encontrado")
        return

    print()
    print(f"- Você esta alterando o usuario {usuario["nome"]} -")
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

    database.usuario.update_one(filtro, { "$set": novoUsuario })