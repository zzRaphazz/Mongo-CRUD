def usuarioMenu():
    execucao = True

    while execucao:
        print("-=-"*20)
        print("Usuários")
        print("1 - Criar Usuário")
        print("2 - Ler Usuário")
        print("3 - Atualizar Usuário")
        print("4 - Deletar Usuário")
        print("0 - Voltar")
        print("-=-"*20)

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("Criar Usuário")
            input()
        elif opcao == "2":
            print("Ler Usuário")
            input()
        elif opcao == "3":
            print("Atualizar Usuário")
            input()
        elif opcao == "4":
            print("Deletar Usuário")
            input()
        elif opcao == "0":
            execucao = False
        else:
            print("Opção inválida!")