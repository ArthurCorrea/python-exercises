# Crie um programa que leia nome, ano de nascimento e carteira
# de trabalho e cadastre-os(com idade) em um dicionário se por
# acaso a CTPS for diferente de zero, o dicionário, receberá
# também o ano de contratação e o salário. Calcule e acrescente
# além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date

nome = str(input('Digite seu nome: '))
ano = int(input('Digite seu ano de nascimento: '))
ctps = int(input('Digite seu CTPS: (0 para "não tenho") '))

inform = {'Nome': nome, 'Idade': date.today().year - ano, 'CTPS': ctps}

dados = list()

if ctps != 0:
    inform['Contrato'] = int(input('Digite o ano em que foi contratado: '))
    inform['Salário'] = float(input('Digite seu salário: R$'))
    print('-=' * 25)
    dados.append(inform.copy())
    for i in dados:
        print(f'Nome: {i["Nome"]}')
        print(f'Idade: {i["Idade"]}')
        print(f'CTPS: {i["CTPS"]}')
        print(f'Você poderá se aposentar em {i["Contrato"] + 35}, '
              f'com {((i["Contrato"] - date.today().year) + i["Idade"] + 35)} anos de idade.')
    print('-=' * 25)

else:
    dados.append(inform.copy())
    print('-=' * 15)
    for i in dados:
        print(f'Nome: {i["Nome"]}')
        print(f'Idade: {i["Idade"]}')
        print('Não possui CTPS.')
