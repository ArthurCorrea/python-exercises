# Faça um programa que leia o sexo de uma pessoa que só aceite os valores 'M'
# ou 'F'. Caso esteja errado, peça a digitação novamente até ter o valor correto.
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Inválido. Favor informar seu sexo corretamente: ')).strip().upper()[0]
print(f'Sexo {sexo} cadrastado com sucesso!')

