salario = float(input("Qual o valor do salário od funcionário que será aumentado?: R$"))
aumento = salario * 0.15
valor = salario + aumento
print("O funcionário teve {:.2f}R$ de aumento, considerando que o salário anterior era {:.2f}R$, portanto, o salário final de seu funcionário será: {:.2f} R$" .format (aumento,salario,valor))
