def num_primp(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
numero_primos = []
for n in range(1,251):
    if num_primp(n):
        numero_primos.append(n)
print("Numero primos entre 1 e 250:")
print(numero_primos)
with open("resultado.txt", "w") as arquivo:
    arquivo.write("Números primos entre 1 e 250:\n")
    for primo in numero_primos:
        arquivo.write(f"{primo}\n")
print("Arquvios salvos com sucesso")
