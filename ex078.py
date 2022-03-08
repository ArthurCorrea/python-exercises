# Crie um programa que leia 5 valores números e guarde-os numa lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e suas respectivas posições na lista.
valores = []
for c in range(1, 6):
    valores.append(int(input(f'Digite o {c}° valor: ')))

print(f'Lista: {valores}')
print(f'O maior valor digitado é {max(valores)} localizado nas posições ', end='')
for i, v in enumerate(valores):
    if v == max(valores):
        print(f'{i + 1}, ', end='')

print()

print(f'O menor valor digitado é {min(valores)} localizado nas posições ', end='')
for c, b in enumerate(valores):
    if b == min(valores):
        print(f'{c + 1}, ', end='')
