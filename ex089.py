# Crie um programa que leia o nome e duas notas de vários alunos
# e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.
print('-='*20)
print('{:^35}'.format('REGISTRE A NOTA DE UM ALUNO'))
print('-='*20)
alunos = list()
while True:
    nome = str(input('Nome do aluno: '))
    nota1 = float(input('Nota do 1° bimestre: '))
    nota2 = float(input('Nota do 2° bimestre: '))
    média = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], média])
    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

print('-=' * 15)
print('{:^35}'.format('BOLETIM GERAL'))
print('--' * 15)
print('{:<3}|{:^15}|{:^15}'.format('N°', 'ALUNO', 'MÉDIA'))
print('--' * 15)
for pos, c in enumerate(alunos):
    print(f'{pos}  |', end='')
    print(f'{c[0]:^14} |', end='')
    print(f'{c[2]:^14}')
print('--' * 15)

while True:
    pergunta = int(input('Deseja acessar as notas de qual aluno? [999 para parar]: '))
    if pergunta == 999:
        print('PROGRAMA FINALIZADO!')
        break
    if pergunta <= len(alunos) - 1:
        print(f'Notas do(a) aluno(a) {alunos[pergunta][0]}: {alunos[pergunta][1]} ')
    print('--'*15)
print(f'{"OBRIGADO!":^15}')

































