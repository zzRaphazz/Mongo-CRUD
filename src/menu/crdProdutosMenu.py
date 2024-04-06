from function.adicionarProdutos import adicionarProdutos
from function.mostrarProdutos import mostrarProdutos
from function.excluirProdutos import excluirProdutos
from database.connection import database
from bson import ObjectId

def crdProdutosMenu(produtos):
    novosProdutos = produtos
    execucao = True
    while execucao:
        print("---"*20)
        print("Produtos da compra")
        print("1 - Adicionar produto")
        print("2 - Ler produtos")
        print("3 - Excluir produto")
        print("0 - Concluir")
        print("---"*20)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            produtoID = str(input("Digite o id do produto: "))
            produtoID = ObjectId(produtoID)
            produtoCompleto = database.produto.find_one({"_id": produtoID})
            if produtoCompleto == None:
                print()
                print("Produto não encontrado!")
                print()
            else:
                produtoNome = produtoCompleto["nome"]
                produtoDescricao = produtoCompleto["descricao"]
                produtoPreco = produtoCompleto["preco"]
            novoProduto = {
                "_id": produtoID,
                "nome": produtoNome,
                "descricao": produtoDescricao,
                "preco": produtoPreco
            }
            novosProdutos = adicionarProdutos(novosProdutos, novoProduto)
        elif opcao == "2":
            mostrarProdutos(novosProdutos)
        elif opcao == "3":
            produtoID = str(input("Digite o id do produto: "))
            produtoID = ObjectId(produtoID)
            novosProdutos = excluirProdutos(produtoID, novosProdutos)
        elif opcao == "0":
            execucao = False
        else:
            print("Opção inválida!")
    return novosProdutos