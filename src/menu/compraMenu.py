from menu.compra.compraCreateMenu import compraCreateMenu
from menu.compra.compraReadMenu import compraReadMenu
from menu.compra.compraUpdateMenu import compraUpdateMenu
from menu.compra.compraDeleteMenu import compraDeleteMenu

def compraMenu():
    execucao = True

    while execucao:
        print("-=-"*20)
        print("compra")
        print("1 - Criar compra")
        print("2 - Ler compra")
        print("3 - Atualizar compra")
        print("4 - Deletar compra")
        print("0 - Voltar")
        print("-=-"*20)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            compraCreateMenu()
        elif opcao == "2":
            compraReadMenu()
        elif opcao == "3":
            compraUpdateMenu()
        elif opcao == "4":
            compraDeleteMenu()
        elif opcao == "0":
            execucao = False
        else:
            print("Opção inválida!")