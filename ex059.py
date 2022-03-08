#  Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] - Somar
# [ 2 ] - Multiplicar
# [ 3 ] - Maior valor
# [ 4 ] - Novos números
# [ 5 ] - Sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
'''escolha = 0
while escolha != 5:
    n1 = int(input('\033[35m1° valor:\033[m '))
    n2 = int(input('\033[36m2° valor:\033[m '))
    print('\033[31m[ 1 ] - SOMAR\033[m
\033[32m[ 2 ] - MULTIPLICAR\033[m
\033[35m[ 3 ] - MAIOR VALOR\033[m
\033[34m[ 4 ] - NOVOS VALORES\033[m
\033[33m[ 5 ] - SAIR\033[m')
    escolha = int(input('\033[1;30mO que deseja fazer?\033[m '))
    if escolha == 1:
        print(f'\033[35m{n1}\033[m + \033[36m{n2}\033[m = \033[32m{n1 + n2}\033[m.')
    if escolha == 2:
        print(f'\033[35m{n1}\033[m x \033[36m{n2}\033[m = \033[32m{n1 * n2}\033[m.')
    if escolha == 3:
        if n1 > n2:
            print(f'O maior valor é \033[35m{n1}\033[m.')
        elif n2 > n1:
            print(f'O maior valor é \033[36m{n2}\033[m.')
        elif n1 == n2:
            print(f'Os valores são iguais.')
    if escolha == 4:
        print('\033[1;30mOk!\033[m')
    if escolha >= 6:
        print('\033[1;31mNúmero inválido. Tente novamente.\033[m')'''

from time import sleep
n1 = int(input('\033[1;30m1° valor: '))
n2 = int(input('2° valor: \033[m'))
escolha = 0
while escolha != 5:
    print('''---> [ 1 ] - SOMAR
---> [ 2 ] - MULTIPLICAR
---> [ 3 ] - MOSTRAR O MAIOR
---> [ 4 ] - NOVOS NÚMEROS
---> [ 5 ] - SAIR DO PROGRAMA''')
    escolha = int(input(f'O que deseja fazer com os valores {n1} e {n2}? '))

    if escolha == 1:
        print(f'{n1} + {n2} = \033[1;31m{n1 + n2}\033[m')

    elif escolha == 2:
        print(f'{n1} x {n2} = \033[1;31m{n1 * n2}\033[m')

    elif escolha == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, o maior é \033[1;31m{n1}\033[m.')
        elif n2 > n1:
            print(f'Entre {n1} e {n2}, o maior é \033[1;31m{n2}\033[m.')
        elif n1 == n2:
            print('Os valores são iguais.')

    elif escolha == 4:
        print('Solicitando novos valores', end='')
        print('.', end='')
        sleep(0.4)
        print('.', end='')
        sleep(0.4)
        print('.')
        sleep(1)
        n1 = int(input('\033[1;30m1° valor: '))
        n2 = int(input('2° valor: \033[m'))

    elif escolha == 5:
        print('ENCERRANDO', end='')
        sleep(0.4)
        print('.', end='')
        sleep(0.4)
        print('.', end='')
        sleep(0.4)
        print('.')
        sleep(0.8)
    else:
        print('ESCOLHA INVÁLIDA. TENTE NOVAMENTE.')
    print('-==' * 15)
    sleep(1.5)

