# Desenvolva um programa que leia o nome de quatro alunos e defina uma ordem
# de apresentação de trabalhos entre eles.
import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
ordem = random.sample([a1, a2, a3, a4], k=4)
print(f'A ordem de apresentação será: \n{ordem}')

# Ou
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
ord = [n1, n2, n3, n4]
random.shuffle(ord)
print(f'A ordem de apresentação será: \n{ord}')
