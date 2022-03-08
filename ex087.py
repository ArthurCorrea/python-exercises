# Aprimore o desafio anterior, mostrando no final:
# A) a soma de todos os valores pares digitados;
# B) a soma dos valores da terceira coluna;
# C) o maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l+1}, {c+1}]: '))

print('-='*20)
print('{:^35}'.format('MATRIZ GERADA'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[l][c]:^5}  ]', end='')
    print()
print('-='*20)

for i in matriz[0]:
    if i % 2 == 0:
        soma += i
for i in matriz[1]:
    if i % 2 == 0:
        soma += i
for i in matriz[2]:
    if i % 2 == 0:
        soma += i
print(f'Soma de todos os números pares: {soma}')
print(f'Soma dos números da 3ª coluna: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'Maior número da 2ª linha: {max(matriz[1][0], matriz[1][1], matriz[1][2])}')
print('-='*20)

