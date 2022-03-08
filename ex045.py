# Crie um programa que faça o computador jogar
# Jokenpô com você.
from random import choice
from time import sleep

print('\033[30mOlá! Vamos jogar Jokenpô!\033[m')

escolha = ['PEDRA', 'PAPEL', 'TESOURA']
escolhacomput = choice(escolha)

print('''\033[35m[1] - PEDRA
[2] - PAPEL
[3] - TESOURA\033[m''')

escolhauser = int(input('\033[31mJogada: \033[m '))

print('\033[34mJO')
sleep(0.7)
print('KEN')
sleep(0.7)
print('PÔ\033[m')
sleep(1)

print('\033[32m-=\033[m' * 17)
print(f'O computador escolheu \033[31m{escolhacomput}\033[m')

if escolhauser == 1:  # jogador jogou PEDRA
    print(f'O jogador escolheu \033[36mPEDRA\033[m')
    if escolhacomput == 'PEDRA':
        print('\033[30mEMPATOU!\033[m')
    if escolhacomput == 'PAPEL':
        print('\033[30mO COMPUTADOR VENCEU!\033[m')
    if escolhacomput == 'TESOURA':
        print('\033[30mO JOGADOR VENCEU!\033[m')

if escolhauser == 2:  # jogador jogou PAPEL
    print(f'O jogador escolheu \033[36mPAPEL\033[m')
    if escolhacomput == 'PAPEL':
        print('\033[30mEMPATOU!\033[m')
    if escolhacomput == 'TESOURA\033[m':
        print('\033[30mO COMPUTADOR VENCEU!\033[m')
    if escolhacomput == 'PEDRA':
        print('\033[30mO JOGADOR VENCEU!\033[m')

if escolhauser == 3:  # jogador jogou TESOURA
    print(f'O jogador escolheu \033[36mTESOURA\033[m')
    if escolhacomput == 'TESOURA':
        print('\033[30mEMPATOU!\033[m')
    if escolhacomput == 'PEDRA':
        print('\033[30mO COMPUTADOR VENCEU!\033[m')
    if escolhacomput == 'PAPEL':
        print('\033[30mO JOGADOR VENCEU!\033[m')

elif escolhauser >= 4:
    print('Opção inválida.')

print('\033[32m-=\033[m' * 17)
print('\033[31mObrigado por jogar!\033[m')
