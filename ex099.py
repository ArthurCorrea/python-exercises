# Faça um programa que tenha uma função chamada maior(), que
# receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual
# deles é o maior.
from time import sleep


def maior(* n):
    print('-='*15)
    print('Analisando os valores passados...')
    for num in n:
        print(f'{num} ', end='')
        sleep(0.5)
    print(f'\nForam informados {len(n)} valores.')
    print(f'Maior valor: {max(n)}')
    print(f'Menor valor: {min(n)}')
    sleep(2.5)


# Programa principal
maior(1, 3, 2, 7, 6, 9)
maior(5, 2, 6)
maior(7, 9, 12, 0, 16, 2, 11, 7, 8)
maior(1, 8, -2, 6, -18, 15)
maior(6, 1, 18, 14, 212, 291, -928, -71, 9824, 10231, 5)
