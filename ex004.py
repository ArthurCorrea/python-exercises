# Crie um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possíveis sobre ele.
n = input('\033[4;35mDigite algo:\033[m')
print('\033[4;30mTipo primitivo:\033[m', type(n))
print('\033[4;31mÉ um número?\033[m', n.isnumeric())
print('\033[4;32mÉ apenas alfabético?\033[m', n.isalpha())
print('\033[4;33mÉ apenas minúsculo?\033[m', n.islower())
print('\033[4;34mÉ apenas maiúsculo?\033[m', n.isupper())
print('\033[4;36mÉ capitalizada?\033[m', n.istitle())

