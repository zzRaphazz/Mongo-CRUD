from database.connection import database

def produtoRead(filter):
    global database
    produto = []

    for product in database.produto.find(filter):
        produto.append(product)
    
    print()
    if produto == []:
        print("Nenhum produto com esse filtro encontrado!")
        input()
    else:
        for product in produto:
            print("_id:", product["_id"])
            print("nome:", product["nome"])
            if product["vendedor"] == {}:
                print("vendedor não encontrado!")
            else:
                print("vendedor:")
                print("     "+"_id:", product["vendedor"]["_id"])
                print("     "+"nome:", product["vendedor"]["nome"])
            print("descricao:", product["descricao"])
            print("preco:", product["preco"])
            print("estoque:", product["estoque"])
            input()

def produtoReadAll():
    global database
    produto = []

    for product in database.produto.find():
        produto.append(product)
    
    print()
    if produto == []:
        print("Nenhum produto encontrado no sistema!")
        input()
    else:
        for product in produto:
            print("_id:", product["_id"])
            print("nome:", product["nome"])
            if product["vendedor"] == {}:
                print("vendedor não encontrado!")
            else:
                print("vendedor:")
                print("     "+"_id:", product["vendedor"]["_id"])
                print("     "+"nome:", product["vendedor"]["nome"])
            print("descricao:", product["descricao"])
            print("preco:", product["preco"])
            print("estoque:", product["estoque"])
            input()