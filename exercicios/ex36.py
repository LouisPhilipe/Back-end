salario = float(input("Salário do comprador: R$"))
financiamento = int(input("Quantos anos de financiamento?"))
casa = float(input("Valor da casa: R$"))

prestacao = casa / (financiamento * 12)

if prestacao <= salario * 0.3:
    print("Para pagar uma casa de {} em {} anos a prestação será de R${:.2f}. Empréstimo aprovado."
          .format(casa, financiamento, prestacao))
else:
    print("Para pagar uma casa de {} em {} anos a prestação será de R${:.2f}. Empréstimo negado."
          .format(casa, financiamento, prestacao))
