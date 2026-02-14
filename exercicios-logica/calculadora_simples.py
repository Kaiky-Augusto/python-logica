while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        print("\nEscolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        opcao = input("Opção: ")

        if opcao == "1":
            resultado = numero1 + numero2
            operacao = "soma"
        elif opcao == "2":
            resultado = numero1 - numero2
            operacao = "subtração"
        elif opcao == "3":
            resultado = numero1 * numero2
            operacao = "multiplicação"
        elif opcao == "4":
            if numero2 == 0:
                print("Erro: divisão por zero.\n")
                continue
            resultado = numero1 / numero2
            operacao = "divisão"
        else:
            print("Opção inválida.\n")
            continue

        print(f"\nResultado da {operacao}: {resultado}\n")

        continuar = input("Deseja fazer outro cálculo? (s/n): ").lower()
        if continuar != "s":
            print("Programa finalizado.")
            break

    except ValueError:
        print("Entrada inválida. Digite apenas números.\n")
