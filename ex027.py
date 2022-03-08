# Crie um programa que leia o nome completo de uma pessoa, mostrando em
# seguida o primeiro e o último nome dela separadamente.
nome = str(input('Qual o seu nome completo? ')).strip()
n = nome.split()
print(f'Primeiro nome: {n[0]}')
print('Último nome: {}'.format(n[len(n)-1]))

# Ou
name = str(input('Qual é o seu nome completo? ')).strip()
nam = name.split()
print(f'Primeiro nome: {nam[0]}')
print(f'Último nome: {nam[-1]}')



