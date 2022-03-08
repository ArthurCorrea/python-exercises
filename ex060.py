# Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('Digite um número para ver seu fatorial: '))
contador = n
fatorial = 1
print(f'{n}! = ', end='')
while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')

# Usando for
num = int(input('Digite um número para ver seu fatorial: '))
fato = 1
print(f'{num}! = ', end='')
for c in range(num, 0, -1):
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fato *= c
print(f'{fato}')
