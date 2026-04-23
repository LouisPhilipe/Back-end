import math
cate_oposto = float(input("Digite o valor do cateto oposto: "))
cate_adjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = math.hypot(cate_oposto, cate_adjacente)
print("O valor da hipotenusa é {:.2f}".format(hipotenusa))
