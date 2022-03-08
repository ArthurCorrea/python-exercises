# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando
# o total de vitórias consecutivas que ele conquistou
# no final do jogo.
from random import randint
from time import sleep

b = 'PAR OU ÍMPAR'

print('\033[1;32m-=\033[m' * 20)
print('\033[1;32m{:^35}\033[m'.format(b))
print('\033[1;32m-=\033[m' * 20)

soma = contador = 0

while True:

    escolhaUser = int(input('\033[1;30mVamos lá! Diga um valor:\033[m '))

    parouimpar = ' '
    while parouimpar not in 'PpIi':
        parouimpar = str(input('\033[1;30mPar ou Ímpar? [P/I]\033[m ')).strip().upper()[0]

    escolhaComput = randint(0, 10)
    soma = escolhaUser + escolhaComput

    print('\033[1;35mAnalisando', end='')   # Animação
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.\033[m')
    sleep(1)

    print('\033[1;30m==\033[m' * 20)
    print(f'O jogador escolheu \033[1;36m{escolhaUser}\033[m e o computador escolheu \033[1;34m{escolhaComput}\033[m.')
    print(f'A soma desses números é \033[1;31m{soma}\033[m ', end='')

    if parouimpar == 'P':
        if soma % 2 == 0:
            print('→ \033[1;35mDEU PAR\033[m')
            print('\033[1;30mO JOGADOR VENCEU!!\033[m')
            contador += 1
        elif soma % 2 == 1:
            print('→ \033[1;35mDEU ÍMPAR\033[m')
            print('\033[1;30mO COMPUTADOR VENCEU!!\033[m')
            break

    elif parouimpar == 'I':
        if soma % 2 == 1:
            print('→ \033[1;35mDEU ÍMPAR\033[m')
            print('\033[1;30mO JOGADOR VENCEU!!\033[m')
            contador += 1
        elif soma % 2 == 0:
            print('→ \033[1;35mDEU PAR\033[m')
            print('\033[1;30mO COMPUTADOR VENCEU!!\033[m')
            break

    print('\033[1;34mVamos jogar novamente...\033[m')
    print('\033[1;30m==\033[m' * 20)

print('\033[1;31m-=\033[m' * 20)
a = 'FIM DE JOGO'
print('\033[1;30m{:^40}\033[m'.format(a))
print(f'Você conseguiu vencer \033[1;34m{contador}\033[m vezes!')
print('\033[1;31m-=\033[m' * 20)

