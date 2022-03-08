# Crie um programa que tenha uma função fatorial() que receba dois
# parâmetros: o primeiro que indique o número a calcular e o outro
# chamado show, que será um valor lógico(opcional) indicando se
# será mostrado ou não na tela o processo de cálculo do fatorial.
from math import factorial


def fatorial(n, show):
    f = n
    resp = show
    if resp == 0:
        for c in range(f, 0, -1):
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
        print(f'{factorial(f)}')
    else:
        print(factorial(f))


while True:
    fatorial(int(input('Digite um número para calcular seu fatorial: ')),
             show=int(input('Deseja ver o cálculo? [0 para SIM / 1 para NÃO] ')))
    print('-='*20)
    sn = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while sn not in 'SN':
        str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if sn == 'N':
        break
    print('-='*20)
    print('PROGRAMA ENCERRADO!')

print('-='*20)

# Resolução do professor


def fato(n, show=False):
    """
    → Calcula o fatorial de um número.
    :param n: número a ser calculado;
    :param show: mostra ou não o cálculo;
    :return: retorna o valor do fatorial de n.
    """
    m = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        m *= c
    return m


print(fato(6, show=True))
