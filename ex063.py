# Escreva um programa que leia um número n inteiro qualquer e mostre
# na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
print('=='*12)
print('Sequência de Fibonnaci')
print('=='*12)
num = int(input('Digite o tamanho da sequência: '))
t1 = 0
t2 = 1
print('--'*20)
print(f'{t1} → {t2}', end='')
contador = 3
while contador <= num:
    t3 = t1 + t2
    print(f' → {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
print(' → FIM')
print('--'*20)
