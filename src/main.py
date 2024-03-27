from menu.comprasMenu import comprasMenu
from menu.produtosMenu import produtosMenu
from menu.usuarioMenu import usuarioMenu
from menu.vendedorMenu import vendedorMenu

execucao = True

while execucao:
    print("==="*10)
    print("Olá, seja bem-vindo ao sistema de CRUD!")
    print("1 - Compras")
    print("2 - Produtos")
    print("3 - Usuários")
    print("4 - Vendedores")
    print("0 - Sair")
    print("==="*10)

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        comprasMenu()
    elif opcao == "2":
        produtosMenu()
    elif opcao == "3":
        usuarioMenu()
    elif opcao == "4":
        vendedorMenu()
    elif opcao == "0":
        print("Adeus...")
        execucao = False
    else:
        print("Opção inválida!")
