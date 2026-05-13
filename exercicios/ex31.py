km = float(input("Digite quantos KMs você percorreu: "))
if km < 200:
    cal = km * 0.50
    print("Você percorreu: {} km e pagará um valor de: R${:.2f}".format(km, cal))
else:
    cal2 = km * 0.45
    print("Você percorreu: {} km e pagará um valor de: R${:.2f}".format(km, cal2))
