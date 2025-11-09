# Classificador de Idade
idade = int(input("Digite sua idade: "))

if idade <= 12:
    categoria = "Criança"
elif idade <= 17:
    categoria = "Adolescente"
elif idade <= 59:
    categoria = "Adulto"
else:
    categoria = "Idoso"

print("Você é:", categoria)
