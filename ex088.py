# Desenvolva um programa que ajude um jogador da MEGA SENA
# a criar palpites. O programa vai perguntar quantos jogos
# serão gerados e vai sortear 6 números entre 1 e 60 para
# cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('-='*20)
print('{:^35}'.format('PALPITES DA MEGA SENA'))
print('-='*20)
escolha = int(input('Quantos jogos deseja que eu sorteie? '))
print('-='*20)
palpites = []
for c in range(0, escolha):
    jogos = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    jogos.sort()
    print(f'{c + 1}° Jogo: {jogos}')
    sleep(1)
print('-='*6, 'BOA SORTE!', '-='*6)

# Outra forma, sem repetição de números
lista = list()
print('-='*20)
print('{:^35}'.format('PALPITES DA MEGA SENA'))
print('-='*20)
quant = int(input('Quantos jogos deseja que eu sorteie? '))
print('-='*20)
for j in range(0, quant):
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    joojs = lista[:]
    lista.clear()
    joojs.sort()
    print(f'{j + 1}º jogo: {joojs}')
    sleep(1)
print('-=-=-=-=-=-= BOA SORTE! -=-=-=-=-=-=')
