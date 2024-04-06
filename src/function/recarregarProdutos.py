from database.produto.produtoUpdate import produtoUpdate

def recarregarProdutos(vendedor):
    for produto in vendedor["produtos"]:
        novoProduto = {
            "vendedor": {
                "_id": vendedor["_id"],
                "nome": vendedor["nome"]
            }
        }
        produtoUpdate({"_id": produto["_id"]}, novoProduto)
