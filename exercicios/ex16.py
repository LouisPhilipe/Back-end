carro = float(input("Digite a quantidade de dias em que você está utilizando o carro:"))
km = float(input("Digite a quantidade de KMs rodados com o carro:"))
valorcarro = carro * 60
valorkm = km * 1.5
valorfinal = valorcarro + valorkm
print("Você utilizou o carro alugado por {:.2f} dias e percorreu {:.2f} KMs, portanto, somando os valores, a dívida será de: {:.2f}" .format(carro,km,valorfinal))
