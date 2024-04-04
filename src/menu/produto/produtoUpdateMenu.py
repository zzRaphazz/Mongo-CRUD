from database.produto.produtoUpdate import produtoUpdate

def produtoUpdateMenu():
    filtro = {
        "nome": str(input("Digite o nome do produto: ")).lower()
    }

    if filtro["nome"] == "":
        print()
        print("Nome não pode ser vazio!")
        input()
        return
    
    produtoUpdate(filtro)
