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
            print("ID:", product["_id"])
            print("Nome:", product["nome"])
            print("Descrição:", product["descricao"])
            print("Preço:", product["preco"])
            print("Estoque:", product["estoque"])

            print("Vendedor:")
            print("     "+"ID:", product["vendedor"]["_id"])
            print("     "+"Nome:", product["vendedor"]["nome"])

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
            print("ID:", product["_id"])
            print("Nome:", product["nome"])
            print("Descrição:", product["descricao"])
            print("Preço:", product["preco"])
            print("Estoque:", product["estoque"])

            print("Vendedor:")
            print("     "+"ID:", product["vendedor"]["_id"])
            print("     "+"Nome:", product["vendedor"]["nome"])

            input()