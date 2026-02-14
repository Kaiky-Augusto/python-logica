try:
    inicio = int(input("Digite o número inicial: "))
    fim = int(input("Digite o número final: "))

    if inicio > fim:
        print("O número inicial não pode ser maior que o final.")
    else:
        quantidade_pares = 0

        for numero in range(inicio, fim + 1):
            if numero % 2 == 0:
                quantidade_pares += 1

        print(f"Quantidade de números pares: {quantidade_pares}")

except ValueError:
    print("Entrada inválida. Digite apenas números inteiros.")
