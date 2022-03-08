# Crie um programa que tenha uma função chamada voto() que vai
# receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições


def voto(ano=0):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO VOTA!')
    elif 18 <= idade < 65:
        print('VOTO OBRIGATÓRIO!')
    elif 16 <= idade < 18:
        print('VOTO OPCIONAL!')
    else:
        print('VOTO OPCIONAL!')


n = int(input('Digite seu ano de nascimento: '))
voto(n)
