# Crie um programa uma matriz de dimensão 3x3 e preencha
# com valores lidos pelo teclado. No final, mostre a
# matriz na tela, com a formatação correta.
print('-=' * 20)
print('{:^35}'.format('CRIAÇÃO DE MATRIZ'))
print('-=' * 20)
total = list()
for co in range(0, 3):
    for li in range(0, 3):
        total.append(int(input(f'Digite um número para a posição [{co}][{li}]: ')))

print('-='*20)
print('{:^35}'.format('MATRIZ GERADA'))
print(f'''    [  {total[0]}  ]    [  {total[3]}  ]    [  {total[6]}  ]
    [  {total[1]}  ]    [  {total[4]}  ]    [  {total[7]}  ]
    [  {total[2]}  ]    [  {total[5]}  ]    [  {total[8]}  ]''')
print('-='*20)

# Outra forma de resolver
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-='*20)
print('{:^35}'.format('MATRIZ GERADA'))
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[  {matriz[l][c]:^5}  ]', end='')
    print()
print('-='*20)
