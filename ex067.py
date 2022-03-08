# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado fo negativo.
from time import sleep

while True:

    escolha = int(input('\033[1;30mDe qual valor deseja ver a tabuada?\033[m '))
    print('\033[1;31m-\033[m' * 25)

    if escolha < 0:
        break
    else:
        for c in range(1, 11):
            print(f'\033[1;30m→ {escolha} x {c} = {escolha * c}\033[m')

    print('\033[1;31m-\033[m' * 25)

print('\033[1;30mAnalisando', end='')
sleep(0.4)
print('.', end='')
sleep(0.4)
print('.', end='')
sleep(0.4)
print('.\033[m')
sleep(1)
print('\033[1;31mPROGRAMA ENCERRADO!\033[m')


