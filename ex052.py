# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[36m', end=' ')
        total += 1
    else:
        print(f'\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número \033[36m{num}\033[m foi dividido \033[32m{total}\033[m vezes.')
if total == 2:
    print('Esse número É PRIMO.')
else:
    print('Esse número NÃO É PRIMO.')

