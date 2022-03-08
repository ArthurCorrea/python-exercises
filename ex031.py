# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km
# e R$0,45 para viagens mais longas.
d = float(input('Quantos Km foram percorridos na viagem? '))
preço200 = d * 0.5
preçomaior = d * 0.45
if d < 200.0:
    print(f'O valor total é R${preço200}!')
else:
    print(f'O valor total é R${preçomaior}!')





