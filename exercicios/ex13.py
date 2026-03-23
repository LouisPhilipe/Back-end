produto = float(input("Qual o preço do produto que será descontado?: R$"))
desconto = produto * 0.05
valor = produto - desconto
print("Considerando que seu produto custa {:.2f} reais, com o desconto de 5%, o valor final de seu produto será: {:.2f} R$" .format (produto,valor))
