# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# - O primeiro valor é maior;
# - O segundo valor é maior;
# - Não existe valor maior, os dois são iguais.
n1 = float(input('\033[31mPrimeiro valor:\033[m '))
n2 = float(input('\033[36mSegundo valor:\033[m '))
if n1 > n2:
    print('O primeiro é o maior valor.')
elif n2 > n1:
    print('O segundo é o maior valor.')
else:
    print('Não existe valor maior, os dois são iguais.')

