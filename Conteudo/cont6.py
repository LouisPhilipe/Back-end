import math
num = int(input('Digite um número: ' ))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #arrendonda para cima
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz))) #arredonda para baixo



from math import sqrt, floor, ceil
num = int(input('Digite um número: ' ))
raiz = sqrt(num)
print('a raiz de {} arredondada para maior é igual a {}'.format(num, ceil(raiz))) #arredonda pra cima
print('a raiz de {} arredondada para menor é igual a {}'.format(num, floor(raiz))) #arredonda para baixo 
