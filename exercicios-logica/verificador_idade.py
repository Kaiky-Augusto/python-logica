while True:
    try:
        idade = int(input("Digite sua idade: "))

        if idade < 0:
            print("Idade inválida.\n")
        elif idade < 18:
            print("Você é menor de idade.\n")
        elif idade < 65:
            print("Você é maior de idade.\n")
        else:
            print("Você é idoso.\n")

        continuar = input("Deseja verificar outra idade? (s/n): ").lower()
        if continuar != "s":
            print("Programa finalizado.")
            break

    except ValueError:
        print("Entrada inválida. Digite um número.\n")
