# Desenvolva um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários
# em uma lista. No final, mostre:
# A) quantas pessoas foram cadastradas;
# B) a média de idade do grupo;
# C) uma lista com todas as mulheres;
# D) uma lista com todas as pessoas com idade acima da média.
print('-=' * 20)
print(f'{"CADASTRE UMA PESSOA":^35}')
print('-=' * 20)

pessoas = list()
p = dict()
totalidade = 0


def pont():
    print('-=' * 20)


while True:
    nome = str(input('Nome: ')).strip()
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        print('ERRO! Digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    idade = int(input('Idade: '))
    totalidade += idade
    p['Nome'] = nome
    p['Sexo'] = sexo
    p['Idade'] = idade
    pessoas.append(p.copy())
    resposta = str('Quer continuar? [S/N] ').strip().upper()[0]
    pont()
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    pont()
    if resposta == 'N':
        break

print(f'\033[1;30mA)\033[m - Um total de {len(pessoas)} pessoas foram cadastradas.')
print(f'\033[1;30mB)\033[m - A média de idade do grupo é de {totalidade / len(pessoas):.1f} anos.')
print(f'\033[1;30mC)\033[m - Mulheres do grupo: ', end='')
for d in pessoas:
    if d['Sexo'] == 'F':
        print(f'\033[1;30m→{d["Nome"]}\033[m', end=' ')
print(f'\n\033[1;30mD)\033[m - Pessoas acima da média de idade: ')
for d in pessoas:
    if d['Idade'] > totalidade / len(pessoas):
        print(f'--> Nome = {d["Nome"]}; Sexo = {d["Sexo"]}; Idade = {d["Idade"]};')
pont()

# Resolução do professor
pessoa = dict()
galera = list()
soma = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Digite corretamente.')
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite corretamente.')
    if resp == 'N':
        break
pont()
print(f'A) - Foram cadastradas {len(galera)} pessoas.')
print(f'B) - A média de idade do grupo é de {soma / len(galera):.2f} anos.')
print(f'C) - Mulheres do grupo: ', end='')
for d in galera:
    if d['Sexo'] == 'F':
        print(f'{d["Nome"]}', end=' ')
print()
print(f'D) - Pessoas com idade acima da média: ')
for p in galera:
    if p['Idade'] > soma / len(galera):
        print(' ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
pont()
