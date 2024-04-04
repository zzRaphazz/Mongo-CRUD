from menu.produto.produtoCreateMenu import produtoCreateMenu
from menu.produto.produtoReadMenu import produtoReadMenu
from menu.produto.produtoUpdateMenu import produtoUpdateMenu
from menu.produto.produtoDeleteMenu import produtoDeleteMenu

def produtoMenu():
    execucao = True

    while execucao:
        print("-=-"*20)
        print("produto")
        print("1 - Criar produto")
        print("2 - Ler produto")
        print("3 - Atualizar produto")
        print("4 - Deletar produto")
        print("0 - Voltar")
        print("-=-"*20)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            produtoCreateMenu()
        elif opcao == "2":
            produtoReadMenu()
        elif opcao == "3":
            produtoUpdateMenu()
        elif opcao == "4":
            produtoDeleteMenu()
        elif opcao == "0":
            execucao = False
        else:
            print("Opção inválida!")