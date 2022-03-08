# Crie um programa que leia vários números inteiros. No final, mostre
# a média entre todos os valores e qual foi o maior e o menor valores
# lidos. O programa deve perguntar ao usuário se ele quer ou não
# continuar digitando valores.
resposta = 'S'
somaval = quantidadeval = maiorn = menorn = 0
while resposta == 'S':
    n = int(input(f'\033[1;30mDigite um valor:\033[m '))
    somaval += n
    quantidadeval += 1
    if quantidadeval == 1:
        maiorn = n
        menorn = n
    else:
        if n > maiorn:
            maiorn = n
        if n < menorn:
            menorn = n
        else:
            menorn = maiorn
    resposta = str(input('\033[1;34mQuer continuar [S/N]?\033[m ')).upper().strip()[0]

média = somaval / quantidadeval
print(f'\033[1;30mO menor valor lido foi\033[m \033[1;31m{menorn}\033[m.')
print(f'\033[1;30mO maior valor lido foi\033[m \033[1;35m{maiorn}\033[m.')
print(f'A soma dos \033[1;34m{quantidadeval}\033[m números que você digitou é', end=' ')
print(f'\033[1;32m{somaval}\033[m.\nA média entre eles é \033[1;36m{média:.1f}\033[m.')



