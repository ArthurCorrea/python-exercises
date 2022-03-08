# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já atingiram.
from datetime import date
totalmenor = 0
totalmaior = 0
atual = date.today().year
for c in range(1, 8):
    ano = int(input(f'Em qual ano a {c}° pessoa nasceu? '))
    idade = atual - ano
    if idade < 21:
        totalmenor += 1
    elif idade >= 21:
        totalmaior += 1
print(f'Temos no grupo {totalmenor} menores de idade e {totalmaior} maiores de idade.')



