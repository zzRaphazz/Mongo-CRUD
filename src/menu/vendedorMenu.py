def vendedorMenu():
    execucao = True

    while execucao:
        print("-=-"*10)
        print("Vendedores")
        print("1 - Criar Vendedor")
        print("2 - Ler Vendedor")
        print("3 - Atualizar Vendedor")
        print("4 - Deletar Vendedor")
        print("0 - Voltar")
        print("-=-"*10)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("Criar Vendedor")
            input()
        elif opcao == "2":
            print("Ler Vendedor")
            input()
        elif opcao == "3":
            print("Atualizar Vendedor")
            input()
        elif opcao == "4":
            print("Deletar Vendedor")
            input()
        elif opcao == "0":
            execucao = False
        else:
            print("Opção inválida!")