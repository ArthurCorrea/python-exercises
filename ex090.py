# Faça um programa que leia o nome e média de um aluno,
# guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.


def pon():
    print('-=' * 10)


nome = str(input('Nome do aluno: '))
média = float(input(f'Média de {nome}: '))
pon()
notas = {'Nome': nome, 'Média': média}
if média >= 7.0:
    notas['Situação'] = 'Aprovado'
elif 5.0 <= média < 7.0:
    notas['Situação'] = 'Recuperação'
else:
    notas['Situação'] = 'Reprovado'
total = list()
total.append(notas.copy())
print('-=' * 15)

for v in total:
    print(f'Aluno: {v["Nome"]}')
    print(f'Média: {v["Média"]}')
    print(f'Situação desse aluno: {v["Situação"]}')
print('-=' * 4, 'FIM DO PROGRAMA', '-=' * 4)

# Ou
aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
pon()
if aluno['Média'] >= 7.0:
    aluno['Situação'] = 'Aprovado'
elif 5.0 <= aluno['Média'] < 7.0:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'

for k, i in aluno.items():
    print(f'{k} → {i}')
pon()
