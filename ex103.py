# Faça um programa que tenha uma função chamada ficha() que receba
# dois parâmetros opcionais: o nome de um jogador e quantos gols ele
# marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome='', gols=0):
    if nome == '' and gols == '':
        print(f'O jogador <desconhecido> marcou 0 gols.')
    elif nome == '':
        print(f'O jogador <desconhecido> marcou {gols} gols.')
    elif gols == '':
        print(f'O jogador {nome} marcou 0 gols.')
    else:
        print(f'O jogador {nome} marcou {gols} gols.')


ficha(str(input('Nome do jogador: ')), str(input('Número de gols: ')))
