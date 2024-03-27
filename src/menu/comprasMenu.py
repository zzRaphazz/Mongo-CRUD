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
            print("Criar Compra")
            input()
        elif opcao == "2":
            print("Ler Compra")
            input()
        elif opcao == "3":
            print("Atualizar Compra")
            input()
        elif opcao == "4":
            print("Deletar Compra")
            input()
        elif opcao == "0":
            execucao = False
        else:
            print("Opção inválida!")