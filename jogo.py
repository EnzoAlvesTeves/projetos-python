import random

print(" Bem-vindo ao jogo de adivinhação!")
print(" Tente adivinhar o número que estou pensando.")
numero = random.randint(1, 10)
isGuessRight = False
while isGuessRight != True:
    chute = input("Digite um número entre 1 e 10: ")
    if int(chute)  == numero:
        print("Parabéns! Você adivinhou o número.")
        isGuessRight = True
    else:
        print("Errado! Tente novamente.")
