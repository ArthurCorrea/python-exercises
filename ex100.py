# Crie um programa que tenha uma lista chamada números e duas
# funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e
# a segunda função vai mostrar a soma entre todos os valores
# PARES sorteados pela função anterior.
from random import randint
from time import sleep


def sorteia():
    soma = 0
    valores = [randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15), randint(1, 15)]
    print(f'5 valores sorteados: ', end='')
    for item in valores:
        print(f'{item} ', end='')
        sleep(0.3)
    for n in valores:
        if n % 2 == 0:
            soma += n
    sleep(1)
    print(f'\nSoma de todos os números pares: {soma}')


sorteia()
print('-='*20)

# Resolução do professor


def sorteie(lista):
    print('Sorteando 5 valores: ', end='')
    for cont in range(0, 5):
        n = randint(1, 15)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)


def somaPar(lista):
    som = 0
    for valor in lista:
        if valor % 2 == 0:
            som += valor
    sleep(1)
    print(f'\nA soma entre todos os valores pares dessa lista é {som}.')


nums = []
sorteie(nums)
somaPar(nums)




