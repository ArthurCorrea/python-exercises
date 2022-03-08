# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# A) quantas pessoas têm mais de 18 anos;
# B) quantos homens foram cadastrados;
# C) quantas mulheres têm menos de 20 anos.
contador = maior18 = totalhomens = mulheres18 = 0

while True:
    print('\033[1;30m-------- CADASTRE UMA PESSOA --------')
    idade = int(input('Idade: '))

    sexo = str(input('Sexo: [M/F]\033[m ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        print('\033[1;35mFavor digitar corretamente.')
        sexo = str(input('Sexo: [M/F]\033[m ')).strip().upper()[0]

    print('\033[1;30m==' * 20)

    escolha = str(input('Deseja continuar? [S/N]\033[m ')).strip().upper()[0]
    while escolha != 'S' and escolha != 'N':
        print('\033[1;35mFavor digitar corretamente.')
        escolha = str(input('Deseja continuar? [S/N]\033[m ')).strip().upper()[0]

    if idade > 18:
        maior18 += 1

    if sexo == 'M':
        totalhomens += 1

    if idade < 20 and sexo == 'F':
        mulheres18 += 1

    contador += 1

    if escolha == 'N':
        break

print('\033[1;31m==\033[m'*30)
print(f'\033[1;31m{contador}\033[m pessoas foram cadastradas.')
print(f'Destas, \033[1;36m{maior18}\033[m pessoa(s) tem mais de 18 anos,')
print(f'\033[1;35m{totalhomens}\033[m são homens', end='')
print(f' e \033[1;34m{mulheres18}\033[m mulher(es) com menos de 20 anos.')
print('\033[1;31m==\033[m'*30)


