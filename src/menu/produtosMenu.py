def produtosMenu():
    execusao = True

    while execusao:
        print("-=-"*10)
        print("Produtos")
        print("1 - Criar Produto")
        print("2 - Ler Produto")
        print("3 - Atualizar Produto")
        print("4 - Deletar Produto")
        print("0 - Voltar")
        print("-=-"*10)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("Criar Produto")
            input()
        elif opcao == "2":
            print("Ler Produto")
            input()
        elif opcao == "3":
            print("Atualizar Produto")
            input()
        elif opcao == "4":
            print("Deletar Produto")
            input()
        elif opcao == "0":
            execusao = False
        else:
            print("Opção inválida!")