while True:
    try:
        salario = float(input("Digite o salário: R$ "))

        if salario <= 0:
            print("Salário inválido.\n")
        elif salario <= 2000:
            imposto = 0
        elif salario <= 3000:
            imposto = salario * 0.08
        elif salario <= 4500:
            imposto = salario * 0.18
        else:
            imposto = salario * 0.28

        if salario > 2000:
            print(f"Imposto a pagar: R$ {imposto:.2f}\n")
        else:
            print("Isento de imposto.\n")

        continuar = input("Deseja calcular novamente? (s/n): ").lower()
        if continuar != "s":
            print("Programa finalizado.")
            break

    except ValueError:
        print("Entrada inválida. Digite um número.\n")
