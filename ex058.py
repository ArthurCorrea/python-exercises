# Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número
# entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.
import random
from time import sleep
# OUTRA FORMA DE FAZER ESTE EXERCÍCIO
'''
escolhaComput = 1
escolhaUser = 0
palpites = 0
while escolhaUser != escolhaComput:
    escolhaComput = random.randint(0, 10)
    escolhaUser = int(input('Escolha um número entre 0 e 10: '))
    print('\033[34mAnalisando', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.\033[m')
    sleep(0.8)
    if escolhaUser != escolhaComput:
        print(f'O computador escolheu {escolhaComput}. \n\033[1;31mVOCÊ ERROU.\033[m')
        palpites += 1
    else:
        print(f'O computador escolheu {escolhaComput}. \n\033[1;32mVOCÊ ACERTOU.\033[m')
print(f'Você acertou em \033[1;34m{palpites}\033[m tentativas. \n\033[1;30mPARABÉNS!!\033[m')'''

# Ou
resposta = str(input('\033[1;34mOlá! Vamos jogar um jogo? [S/N]\033[m ')).strip().upper()[0]
if resposta == 'S':
    print('Ótimo! Você deve tentar adivinhar um número que pensei entre \033[1;30m0\033[m e \033[1;30m10\033[m.')
    escolhaUser = int(input('\033[1;35mVamos lá, em qual número você acha que pensei?\033[m '))
    print('\033[1;31mAnalisando', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.\033[m')
    sleep(0.8)
    escolhaComput = random.randint(0, 10)
    contador = 0
    while escolhaUser != escolhaComput:
        contador += 1
        if escolhaUser > escolhaComput:
            print('Um pouco menos.')
        elif escolhaUser < escolhaComput:
            print('Um pouco mais.')
        escolhaUser = int(input('\033[1;30mTente novamente: \033[m'))
        print('\033[1;31mAnalisando', end='')
        sleep(0.4)
        print('.', end='')
        sleep(0.4)
        print('.', end='')
        sleep(0.4)
        print('.\033[m')
        sleep(0.8)
    print(f'\033[1;30mPARABÉNS!!\033[m')
    print(f'Você acertou com \033[1;34m{contador + 1}\033[m tentativas!')

elif resposta == 'N':
    print('Tudo bem... Talvez numa próxima...')
    print('Adeus!!')







