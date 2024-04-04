from menu.vendedor.vendedorCreateMenu import vendedorCreateMenu
from menu.vendedor.vendedorReadMenu import vendedorReadMenu
from menu.vendedor.vendedorUpdateMenu import vendedorUpdateMenu
from menu.vendedor.vendedorDeleteMenu import vendedorDeleteMenu

def vendedorMenu():
    execucao = True

    while execucao:
        print("-=-"*20)
        print("Vendedores")
        print("1 - Criar vendedor")
        print("2 - Ler vendedor")
        print("3 - Atualizar vendedor")
        print("4 - Deletar vendedor")
        print("0 - Voltar")
        print("-=-"*20)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            vendedorCreateMenu()
        elif opcao == "2":
            vendedorReadMenu()
        elif opcao == "3":
            vendedorUpdateMenu()
        elif opcao == "4":
            vendedorDeleteMenu()
        elif opcao == "0":
            execucao = False
        else:
            print("Opção inválida!")