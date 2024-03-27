from menu.compras.comprasCreateMenu import comprasCreateMenu
from menu.compras.comprasReadMenu import comprasReadMenu
from menu.compras.comprasUpdateMenu import comprasUpdateMenu
from menu.compras.comprasDeleteMenu import comprasDeleteMenu

def comprasMenu():
    execucao = True

    while execucao:
        print("-=-"*10)
        print("Compras")
        print("1 - Criar Compra")
        print("2 - Ler Compra")
        print("3 - Atualizar Compra")
        print("4 - Deletar Compra")
        print("0 - Voltar")
        print("-=-"*10)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            comprasCreateMenu()
        elif opcao == "2":
            comprasReadMenu()
        elif opcao == "3":
            comprasUpdateMenu()
        elif opcao == "4":
            comprasDeleteMenu()
        elif opcao == "0":
            execucao = False
        else:
            print("Opção inválida!")