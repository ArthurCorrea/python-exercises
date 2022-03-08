# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
maiorp = 0
menorp = 0
for p in range(1, 6):
    peso = float(input(f'Qual o peso da {p}° pessoa? KG '))
    if p == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print(f'A pessoa mais leve tem {menorp}Kg e a mais pesada tem {maiorp}Kg')


