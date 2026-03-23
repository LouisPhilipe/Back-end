largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {} x {} e sua área é de {:.2f} m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisa de {:.2f} litros de tinta.'.format(area / 2))
