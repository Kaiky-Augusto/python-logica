soma = 0

while True:
    try:
        numero = int(input("Digite um número (0 para sair): "))

        if numero == 0:
            break

        soma += numero

    except ValueError:
        print("Entrada inválida. Digite um número.")

print(f"Soma total: {soma}")
