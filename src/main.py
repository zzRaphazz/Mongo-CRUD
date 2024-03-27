from menu.comprasMenu import comprasMenu

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
        print("Produtos")
        input()
    elif opcao == "3":
        print("Usuários")
        input()
    elif opcao == "4":
        print("Vendedores")
        input()
    elif opcao == "0":
        print("Adeus...")
        execucao = False
    else:
        print("Opção inválida!")
