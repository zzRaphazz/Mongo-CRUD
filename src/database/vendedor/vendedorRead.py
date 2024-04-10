from database.connection import database

def vendedorRead(filter):
    global database
    vendedor = []

    for v in database.vendedor.find(filter):
        vendedor.append(v)

    print()
    if vendedor == []:
        print("Nenhum vendedor com esse filtro encontrado!")
        input()
    else:
        for v in vendedor:
            print("ID:", v["_id"])
            print("Nome:", v["nome"])
            print("RG:", v["rg"])
            if v["produtos"] == []:
                print("Nenhum produto cadastrado!")
            else:
                for produto in v["produtos"]:
                    print("Produto:")
                    print("     "+"ID:", produto["id"])
                    print("     "+"Nome:", produto["nome"])
                    print("     "+"Descrição:", produto["descricao"])
                    print("     "+"Preço:", produto["preco"])
                    print("     "+"Estoque", produto["estoque"])
                    print()
            input()

def vendedorReadAll():
    global database
    vendedor = []

    for v in database.vendedor.find():
        vendedor.append(v)

    print()
    if vendedor == []:
        print("Nenhum vendedor encontrado no sistema!")
        input()
    else:
        for v in vendedor:
            print("_id:", v["_id"])
            print("nome:", v["nome"])
            print("rg:", v["rg"])
            print("produtos:")    
            if v["produtos"] == []:
                print("     "+"nenhum produto cadastrado!")
            else:
                for produto in v["produtos"]:
                    print("     "+"_id:", produto["_id"])
                    print("     "+"nome:", produto["nome"])
                    print("     "+"descricao:", produto["descricao"])
                    print("     "+"preco:", produto["preco"])
                    print("     "+"--------------------")
            input()