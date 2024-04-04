from menu.compraMenu import compraMenu
from menu.produtoMenu import produtoMenu
from menu.usuarioMenu import usuarioMenu
from menu.vendedorMenu import vendedorMenu

execucao = True

while execucao:
    print("==="*20)
    print("Olá, seja bem-vindo ao sistema de CRUD!")
    print("1 - Compra")
    print("2 - Produto")
    print("3 - Usuario")
    print("4 - Vendedor")
    print("0 - Sair")
    print("==="*20)

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        compraMenu()
    elif opcao == "2":
        produtoMenu()
    elif opcao == "3":
        usuarioMenu()
    elif opcao == "4":
        vendedorMenu()
    elif opcao == "0":
        print("Adeus...")
        execucao = False
    else:
        print("Opção inválida!")
