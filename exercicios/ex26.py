frase = str(input("Digite uma frase: ")).strip().upper()

print("A letra A aparece {} vezes na frase".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A") + 1))  # +1 para ajustar à contagem humana
print("A última letra A apareceu na posição {}".format(frase.rfind("A")))  # procura da direita para a esquerda
