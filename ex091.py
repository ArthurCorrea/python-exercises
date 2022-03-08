# Crie um programa onde 4 jogadores joguem um dado e tenham
# resultados aleatórios. Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o
# vencedor tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
print('\033[1;30m-='*20)
print(f'{"JOGUEM OS DADOS":^35}')
print('\033[1;30m-=\033[m'*20)

jogadores = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
sleep(0.3)

for k, i in jogadores.items():
    print(f'--> O \033[1;30m{k}\033[m tirou o número \033[1;34m{i}\033[m.')
    sleep(0.6)

rank = dict()
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*6, 'RANKING', '-='*6)
cont = 0
for i, p in rank:
    cont += 1
    print(f'\033[1;34m{cont}° lugar\033[m - \033[1;30m{i}\033[m --> \033[1;31m{p}\033[m')
    sleep(0.5)


