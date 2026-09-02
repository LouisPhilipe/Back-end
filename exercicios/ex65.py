from random import randint

print('Vamos jogar par ou ímpar')
cont = 0

while True:
    palpite = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? ')).strip().lower()
    
    pc = randint(1, 10)
    resultado = palpite + pc
    
    if resultado % 2 == 0 and escolha == 'par' or resultado % 2 != 0 and escolha in 'ímpar impar':
        deu = 'par' if resultado % 2 == 0 else 'ímpar'
        print(f'Você jogou {palpite} e o computador jogou {pc}. Total de {resultado} deu {deu}.')
        print('Você VENCEU!')
        cont += 1
        print('Vamos jogar novamente...\n')
    else:
        escolhapc = 'par' if resultado % 2 == 0 else 'ímpar'
        print(f'Você jogou {palpite} e o computador jogou {pc}. Total de {resultado} deu {escolhapc}.')
        print('Você PERDEU!')
        break

print(f'Game Over! Você venceu {cont} vezes.')
