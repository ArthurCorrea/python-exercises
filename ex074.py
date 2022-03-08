# Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla.
# Depois disso, mostre a listagem dos números gerados e também
# indique o menor e o maior valor que estão na tupla.
from random import randint
escolha = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Valores sorteados: ', end='')
for c in escolha:
    print(f'{c}', end=' ')
print(f'\nO maior valor sorteado foi {max(escolha)}.')
print(f'O menor valor sorteado foi {min(escolha)}.')


