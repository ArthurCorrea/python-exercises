# Crie um programa que leia as notas do ano letivo de um aluno e faça a média entre elas.
n = float(input('\033[31mNota do 1° bimestre: \033[m'))
q = float(input('\033[32mNota do 2° bimestre: \033[m'))
r = float(input('\033[36mNota do 3° bimestre: \033[m'))
s = float(input('\033[34mNota do 4° bimestre: \033[m'))
res = (n + q + r + s) / 4
print('A média entre {}, {}, {} e {} é de {:.1f} pontos!'.format(n, q, r, s, res))

