def excluirProdutos(id, produtos):
    for produto in produtos:
        if produto["_id"] == id:
            produtos.remove(produto)
            return produtos
    return produtos