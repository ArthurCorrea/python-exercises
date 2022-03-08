# Escreva uma programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
# pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.
import random
from time import sleep
n1 = [0, 1, 2, 3, 4, 5]
n2 = random.choice(n1)
print('===' * 25)
print('Olá! Bem-vindo ao jogo da adivinhação!')
print('O computador escolherá um número e você deve tentar adivinhá-lo!')
print('===' * 25)
user = int(input('Por favor, escolha um número de 0 a 5: '))
print('Processando...')
sleep(1.5)
if user == n2:
    print(f'Quem diria! Você acertou! O número escolhido pelo computador foi {n2}.')
else:
    print(f'Que pena, você errou! O computador escolheu o número {n2}.')
print('-----------Fim de jogo-----------')

