# Crie um programa que vai ler vários números e colocar numa lista.
# Depois disso, mostre:
# A) quantos números foram digitados;
# B) a lista de valores, ordenada de forma decrescente;
# C) se o valor 5 foi digitado e não está ou não na lista.
valores = []
cont = 0
while True:
    valores.append(int(input('Digite um número: ')))
    cont += 1
    print('-='*20)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('-=' * 25)

print(f'Lista: {valores}')
print(f'Foram digitados {cont} valores.')
valores.sort(reverse=True)
print(f'Lista dos valores em ordem decrescente: {valores}')

if 5 in valores:
    print('Há o valor 5 nesta lista!')
else:
    print('Não encontrei nenhum valor 5 nesta lista.')

print('-=' * 25)
