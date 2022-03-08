# Crie um programa que leia quatro notas de um aluno e calcule
# a sua média, mostrando uma mensagem no final, de acordo com
# a média atingida:
# - Média abaixo de 5.0: "Reprovado!"
# - Média entre 5.0 e 6.9: "Recuperação!"
# - Média 7.0 ou superior: "Aprovado!"
nota1 = float(input('\033[36mNota do 1° bimestre:\033[m '))
nota2 = float(input('\033[31mNota do 2° bimestre:\033[m '))
nota3 = float(input('\033[34mNota do 3° bimestre:\033[m '))
nota4 = float(input('\033[30mNota do 4° bimestre:\033[m '))
média = (nota1 + nota2 + nota3 + nota4) / 4
if média < 5.0:
    print(f'Sua média é {média:.1f}... \n\033[31mVOCÊ FOI REPROVADO!\033[m')
elif 5.0 <= média <= 6.9:
    print(f'Sua média é {média:.1f}... \n\033[31mVOCÊ ESTÁ DE RECUPERAÇÃO!\033[m')
elif média > 7.0:
    print(f'Sua média é {média:.1f}... \n\033[36mVOCÊ FOI APROVADO!\033[m')


