# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# -> A média de idade do grupo;
# -> Qual o nome do homem mais velho;
# -> Quantas mulheres têm menos de 20 anos.
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomehomem = ''
totmulher = 0
for c in range(1, 5):
    print(f'----- {c}° PESSOA -----')
    nome = str(input('Nome: ')).upper().strip()
    idade = int(input('Idade: '))
    print('''[ M ] - MASCULINO\n[ F ] - FEMININO''')
    sexo = str(input('Sexo: ')).upper().strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehomem = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomem = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
médiaidade = somaidade / 4
print(f'A média de idade do grupo é de {médiaidade} anos.')
print(f'O homem mais velho se chama {nomehomem} e tem {maioridadehomem} anos.')
print(f'{totmulher} mulher(es) desse grupo tem menos de 20 anos.')

