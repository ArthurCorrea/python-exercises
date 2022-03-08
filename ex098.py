# Crie um programa que tenha uma função chamada contador(),
# que receba três parâmetros: início, fim e passo e realize
# a contagem. Seu programa tem que realizar três contagens
# através da função criada:
# A) - de 1 até 10, de 1 em 1;
# B) - de 10 até 0, de 2 em 2;
# C) - uma contagem personalizada.

# Minha resolução:
from time import sleep
print('--'*20)
print(f'{"CONTADOR":^35}')


def contador(início, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {início} até {fim} de {passo} em {passo}:')
    for i in range(início, fim, passo):
        print(f'{i}', end=' ')
        sleep(0.3)
    if início >= fim and passo > 0:
        while início >= fim:
            print(f'{início}', end=' ')
            início -= passo
            sleep(0.3)
    print('FIM!')
    print('--' * 20)


contador(1, 10+1, 1)
contador(10, 0-1, 2)
print('Vamos lá! Sua vez de criar uma sequência personalizada!')
contador(início=int(input('Início: ')), fim=int(input('Fim: ')), passo=int(input('Passo: ')))


# Resolução do professor


def contadorr(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(1.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += p
        print('FIM!')
        print('-='*20)
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= p
        print('FIM!')


# Programa Principal
contadorr(1, 10, 1)
contadorr(10, 0, 2)
print('-='*20)
print('Agora é sua vez de criar uma contagem personalizada!')
ini = int(input('Início: '))
fi = int(input('Fim: '))
pas = int(input('Passo: '))
contadorr(ini, fi, pas)
