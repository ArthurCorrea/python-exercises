# Crie um programa que vai ler vários números e colocar numa lista.
# Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados, respectivamente.
# No final, mostre o conteúdo das três listas geradas.
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    print('-=' * 20)
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('-=' * 25)

print(f'Lista total: {valores}')

print('-=' * 25)

print(f'A lista dos números pares é: ', end='')
for p in valores:
    if p % 2 == 0:
        print(f'{p} ', end='')

print('\nA lista dos números ímpares é: ', end='')
for i in valores:
    if i % 2 == 1:
        print(f'{i} ', end='')


