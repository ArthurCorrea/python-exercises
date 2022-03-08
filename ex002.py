# Crie um programa em que você possa digitar seu nome e fazer com que a máquina o repita
nome = input('Olá! Qual é o seu nome? ')
print('É um prazer conhecê-lo,\033[36m', nome+'\033[m!')
# Pode-se fazer o mesmo programa usando:
nome = input('Bem-vindo! Como você se chama? ')
print('Prazer te conhecer, {}{}{}!'.format('\033[31m', nome, '\033[m'))

