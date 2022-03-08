# Desenvolva um programa onde o usuário possa digitar sete
# valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final,
# mostre os valores pares e ímpares em ordem crescente.
valores = []
números = []

for c in range(1, 8):
    números.append(int(input(f'Digite o {c}° valor: ')))
    valores.append(números[:])
    números.clear()

print('-='*20)
valores.sort()
print(f'Lista total: {valores}')
print('-='*20)

print(f'Lista dos números pares: ', end='')
for p in valores:
    if p[0] % 2 == 0:
        print(f'[{p[0]}]', end=' ')
print()
print(f'Lista dos números ímpares: ', end='')
for i in valores:
    if i[0] % 2 == 1:
        print(f'[{i[0]}]', end=' ')
print()
print('-='*40)

# Outra forma de resolver
num = [[], []]
valores = 0
for q in range(1, 8):
    valores = int(input(f'Digite o {q}° valor: '))
    if valores % 2 == 0:
        num[0].append(valores)
    else:
        num[1].append(valores)

num[0].sort()
num[1].sort()
print(f'Lista dos números pares: {num[0]}')
print(f'Lista dos números ímpares: {num[1]}')

