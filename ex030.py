# Crie um programa que leia um número inteiro e mostre
# na tela se ele é par ou ímpar.
import random
n = int(input('Digite um número: '))
resultado = n % 2
if resultado == 0:
    print(f'O número {n} é par!')
else:
    print(f'O número {n} é ímpar!')
