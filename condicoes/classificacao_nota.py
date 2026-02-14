while True:
    try:
        nota = float(input("Digite a nota do aluno (0 a 10): "))

        if nota < 0 or nota > 10:
            print("Nota inválida.\n")
        elif nota < 5:
            print("Aluno reprovado.\n")
        elif nota < 7:
            print("Aluno em recuperação.\n")
        else:
            print("Aluno aprovado.\n")

        continuar = input("Deseja verificar outra nota? (s/n): ").lower()
        if continuar != "s":
            print("Programa finalizado.")
            break

    except ValueError:
        print("Entrada inválida. Digite um número.\n")
