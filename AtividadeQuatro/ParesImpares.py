# Analisador de números: pares e ímpares
quantidade = int(input("Quantos números deseja inserir? "))

pares = 0
impares = 0

for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}º número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
