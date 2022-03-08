# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas
# -> O nome com todas as letras minúsculas
# -> Quantas letras têm (sem considerar espaços)
# -> Quantas letras têm o primeiro nome
nome = str(input('Olá! Qual é o seu nome completo? ')).strip()
print(f'OLÁ, {nome.upper()}!')
print(f'Ops.. Perdão... Prometo não gritar novamente, {nome.lower()}.')
print(f'Ou você prefere mais bonitinho? Tipo {nome.title()}.')
print('Pois bem, vejo que seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
dividido = nome.split()
print(f'Vejo também que o nome {dividido[0]} tem {len(dividido[0])} letras.')

