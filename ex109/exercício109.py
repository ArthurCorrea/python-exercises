from ex109 import moeda

n = float(input('Digite um valor: '))
num = float(input('Em quanto quer diminuir e aumentar esse valor? '))

print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n, True)}.')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}.')
print(f'{moeda.moeda(n)} aumentado em {num:.0f}% é {moeda.aumentar(n, num, True)}.')
print(f'{moeda.moeda(n)} diminuído em {num:.0f}% é {moeda.diminuir(n, num, True)}')

