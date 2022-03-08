# Crie um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer. Quando
# o usuário digitar a palavra "FIM", o programa se encerrará.
# OBS: use cores.


def ajuda(h):
    sos = h
    while True:
        help(f'{sos}')
        resp = str(input('\033[1;30mQuer inserir outro comando? [S/N]\033[m ')).upper().strip()[0]
        while resp != 'S' and resp != 'N':
            resp = str(input('\033[1;30mQuer inserir outro comando? [S/N]\033[m ')).upper().strip()[0]
        if resp == 'N':
            break
        ajuda(str(input('\033[1;30mPrecisa de ajuda em qual comando?\033[m ')))
        print('-='*20)


ajuda(str(input('\033[1;30mPrecisa de ajuda em qual comando?\033[m ')))

# Resolução do professor
cores = ['\033[m',      # 0 - sem cores
         '\033[1;31m',  # 1 - vermelho
         '\033[1;36m',  # 2 - azul
         '\033[1;35m',  # 3 - roxo
         '\033[1;30m']  # 4 - branco
from time import sleep


def aj(com):
    titulo(f'Manual do comando {com}', 1)
    sleep(1)
    print(cores[4], end='')
    help(com)
    print(cores[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(cores[0], end='')


comando = ''
while True:
    sleep(1)
    titulo('SISTEMA PYTHON DE AJUDA', 2)
    comando = str(input('\033[1;30mFunção ou biblioteca:\033[m '))
    if comando.upper() == 'FIM':
        break
    else:
        aj(comando)
titulo('ATÉ MAIS!', 2)
