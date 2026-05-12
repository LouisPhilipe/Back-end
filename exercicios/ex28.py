import random
num = random.randint(1,5)
res = int(input("Digite um número entre 0 a 5: "))
if res == num:
    print("Você acertou o número sorteado!")
else:
    print("Você errou o número sorteado, tente novamente!")
    print("O número sorteado era: {}" .format(num))
