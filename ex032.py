# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Digite um ano qualquer ou digite 0 para analisar o ano atual:  '))
biss = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
if ano == 0:
    ano = date.today().year
if biss:
    print(f'{ano} é um ano bissexto!')
else:
    print(f'{ano} não é um ano bissexto!')


