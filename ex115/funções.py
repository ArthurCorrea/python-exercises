pessoas = ['João', 18, 'Luís', 23, 'Yasmin', 13, 'Jorge', 53, 'Ulisses', 31]
from time import sleep


def lista1():
    print('\033[1;35m-'*30)
    print(f'{"LISTA DAS PESSOAS":^30}')
    print('-'*30)
    for c in pessoas:
        if type(c) == str:
            print(f'\033[1;30m{c}', end='')
        elif type(c) == int:
            print(f'\t{c:>15} anos\033[m')
    print('\033[1;35m-\033[m'*30)
    sleep(1)
    menu()


def menu():
    print('\033[1;34m- '*20)
    print(f'{"MENU DE OPÇÕES":^35}')
    print('- '*20)
    print('\033[1;30m1 - Ver lista das pessoas')
    print('2 - Cadastrar nova pessoa.')
    print('3 - Sair do sistema.\033[m')
    print('\033[1;34m- '*20)
    while True:
        try:
            resp = int(input('\033[1;30mO que deseja fazer? '))
            break
        except:
            print('Por favor, tente novamente.')
            continue
    while resp > 3 or resp < 1:
        print('Por favor, digite uma opção válida.')
        resp = int(input('O que deseja fazer?\033[m '))
    print('\033[1;34m- \033[m'*20)
    sleep(1)
    if resp == 1:
        lista1()
    elif resp == 2:
        adicionar()
    elif resp == 3:
        print(f'\033[1;30m{"OBRIGADO E VOLTE SEMPRE!":^35}\033[m')
        print('\033[1;34m- '*20)
        quit()


def adicionar():
    pessoas.append(str(input('\033[1;30mNome: ')))
    pessoas.append(int(input('Idade: \033[m')))
    sleep(1)
    menu()
