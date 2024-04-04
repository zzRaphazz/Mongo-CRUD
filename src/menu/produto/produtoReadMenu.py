from database.produto.produtoRead import produtoRead, produtoReadAll

def produtoReadMenu():
    
    filtro = {
        "nome": str(input("Digite um nome: ")).lower()
    }

    if filtro["nome"] == "":
        produtoReadAll()
    else:
        produtoRead(filtro)