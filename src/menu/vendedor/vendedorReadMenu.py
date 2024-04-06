from database.vendedor.vendedorRead import vendedorRead, vendedorReadAll

def vendedorReadMenu():
    nome = str(input("Digite um nome: ")).lower()

    if nome == "":
        vendedorReadAll()
        return

    filtro = {
        "nome": nome
    }

    vendedorRead(filtro)
