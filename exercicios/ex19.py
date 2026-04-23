import math

ang = float(input("digite o ângulo que você deseja: "))
seno = math.sin(math.radians(ang))  # os valores têm que ser em radianos, então usamos math.radians
cose = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print("O ângulo de {} tem seno de {:.2f}".format(ang, seno))
print("O ângulo de {} tem coseno de {:.2f}".format(ang, cose))
print("O ângulo de {} tem tangente de {:.2f}".format(ang, tang))
