# Faça um programa que tenha uma função chamada área(), que
# receba as dimensões de um terreno retangular(largura e
# comprimento) e mostre a área do terreno.
print('Controle de Terrenos')
print('-'*20)


def área(larg, comp):
    a = larg * comp
    print(f'{larg}m x {comp}m totaliza uma área de {a}m².')


def p():
    print('--'*20)


while True:
    área(float(input('Largura em metros: ')), float(input('Comprimento em metros: ')))
    p()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    p()
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"PROGRAMA ENCERRADO!"}')
