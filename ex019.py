# Crie um programa que leia o nome de quatro alunos, escolha um deles e mostre na tela.
import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
print(f'O aluno escolhido foi {random.choice(lista)}.')
