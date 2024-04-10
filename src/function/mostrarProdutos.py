def mostrarProdutos(produtos):
    print("Produtos:")
    for produto in produtos:
        print("     "+"_id:", produto["_id"])
        print("     "+"nome:", produto["nome"])
        print("     "+"descricao:", produto["descricao"])
        print("     "+"preco:", produto["preco"])
        print()