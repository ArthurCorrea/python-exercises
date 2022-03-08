# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando
# os dados em forma tabular.
print('=='*25)
print('{:^45}'.format('TABELA DE PREÇOS'))
print('=='*25)
preços = ('Arroz', 2.50, 'Feijão', 4.00, 'Frango', 7.50, 'Bife', 15.00)
for pos in range(0, len(preços)):
    if pos % 2 == 0:
        print(f'{preços[pos]:.<25}', end='')
    else:
        print(f'R${preços[pos]:>6.2f}')
print('=='*25)