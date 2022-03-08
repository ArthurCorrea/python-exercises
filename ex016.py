# Crie um programa que leia um número real qualquer e diga a sua parte inteira.
from math import trunc
n = float(input('Digite um valor: '))
q = trunc(n)
print(f'O número digitado foi {n} e sua porção inteira é {q}!')

# Ou
num = float(input('Digite um valor: '))
print(f'O número digitado foi {num} e sua porção inteira é {trunc(num)}!')

