# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os numa tupla. No final, mostre:
# A) quantas vezes apareceu o valor 9;
# B) em que posição foi digitado o primeiro valor 3;
# C) quais foram os números pares.
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
n4 = int(input('Digite o 4° número: '))
números = (n1, n2, n3, n4)
print('Os valores digitados foram: ', end='')
for c in números:
    print(f'{c}', end=' ')
print(f'\nO número 9 foi digitado {números.count(9)} vezes.')
if 3 in números:
    print(f'O número 3 foi digitado pela primeira vez no {números.index(3) + 1}° número.')
else:
    print(f'O número 3 não foi digitado nenhuma vez.')
print('Os valores pares são: ', end='')
for n in números:
    if n % 2 == 0:
        print(f'{n}', end=' ')
