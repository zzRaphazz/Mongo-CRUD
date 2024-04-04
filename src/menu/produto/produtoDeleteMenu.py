from database.produto.produtoDelete import produtoDelete

def produtoDeleteMenu():
    filtro = {
        "nome": input("Digite o nome do produto: ").lower()
    }

    if filtro["nome"] == "":
        print()
        print("Nome não pode ser vazio!")
        input()
        return
    
    produtoDelete(filtro)
    input()