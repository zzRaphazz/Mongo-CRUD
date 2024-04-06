from database.produto.produtoUpdate import produtoUpdate

def recarregarProdutos(vendedor):
    global database
    for produto in vendedor["produtos"]:
        novoProduto = {
            "vendedor": {
                "_id": vendedor["_id"],
                "nome": vendedor["nome"]
            }
        }
        
        database.produto.update_one({"_id": produto["_id"]}, { "$set": novoProduto })
        