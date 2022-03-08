# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário quer continuar.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.0
# C) qual o nome do produto mais barato.
soma = produtos1000 = quantidade = menorproduto = 0
barato = ''

a = 'LOJÃO DAORA'
print('\033[1;30m==\033[m' * 20)
print('\033[1;30m{:^35}\033[m'.format(a))
print('\033[1;30m==\033[m' * 20)

while True:

    nome = str(input('\033[1;30mNome do produto: ')).strip().lower()
    preço = float(input('Preço do produto: R$'))

    quantidade += 1
    soma += preço

    if preço > 1000.0:
        produtos1000 += 1

    if quantidade == 1:
        menorproduto = preço
        barato = nome
    else:
        if preço < menorproduto:
            menorproduto = preço
            barato = nome

    print('\033[1;35m==\033[m' * 20)
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('\033[1;30mQuer continuar? [S/N]\033[m ')).strip().upper()[0]
    print('\033[1;35m==\033[m' * 20)
    if escolha == 'N':
        break

print('\033[1;31m---------- FIM DAS COMPRAS ----------\033[m')
print(f'Você comprou \033[1;33m{quantidade}\033[m produtos.')
print(f'O total das compras é de \033[1;31mR${soma:.2f}\033[m.')
print(f'\033[1;33m{produtos1000}\033[m produtos custam mais de \033[1;34mR$1000,00\033[m')
print(f'O produto mais barato é \033[1;36m{barato}\033[m e custa \033[1;33mR${menorproduto:.2f}\033[m.')
