# Conversor de Moeda
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolar = valor_reais / taxa_dolar
valor_em_euro = valor_reais / taxa_euro

print("Valor em reais: R$", valor_reais)
print("Em dólares: US$", round(valor_em_dolar, 2))
print("Em euros: €", round(valor_em_euro, 2))
