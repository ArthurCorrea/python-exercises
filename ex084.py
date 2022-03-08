# Crie um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) quantas pessoas foram cadastradas;
# B) uma listagem com as pessoas mais pesadas;
# C) uma listagem com as pessoas mais leves.
print('-='*20)
print('{:^35}'.format('CADASTRE UMA PESSOA'))
print('-='*20)
pessoas = []
peso = []
maiorpeso = menorpeso = 0
while True:
    peso.append(str(input('Nome: ')))
    peso.append(float(input('Peso em KG: ')))
    pessoas.append(peso[:])
    peso.clear()
    print('-='*20)
    resposta = ''
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-='*20)
    if resposta == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print('-='*20)
for c, p in enumerate(pessoas):
    if p[1] >= 90:
        maiorpeso += 1
        print(f'\033[1;30m{p[0]} tem {p[1]}kg, ficando na lista das pessoas mais pesadas.\033[m')
    elif p[1] <= 70:
        menorpeso += 1
        print(f'\033[1;35m{p[0]} tem {p[1]}kg, ficando na lista das pessoas mais leves.\033[m')

print('-='*20)
print(f'\033[1;31m{maiorpeso} pessoas estão na lista dos mais pesados e {menorpeso} estão na lista dos mais leves.\033[m')
