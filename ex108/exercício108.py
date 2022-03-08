from ex108 import moeda

n = float(input('Digite um valor: '))
num = float(input('Em quanto quer diminuir e aumentar esse valor? '))

print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}.')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}.')
print(f'{moeda.moeda(n)} aumentado em {num:.0f}% é {moeda.moeda(moeda.aumentar(n, num))}.')
print(f'{moeda.moeda(n)} diminuído em {num:.0f}% é {moeda.moeda(moeda.diminuir(n, num))}')

