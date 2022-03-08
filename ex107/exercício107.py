from ex107 import moeda

n = int(input('Digite um valor: '))
num = float(input('Em quanto quer diminuir e aumentar esse valor? '))

print(f'O dobro de {n} é {moeda.dobro(n)}.')
print(f'A metade de {n} é {moeda.metade(n)}.')
print(f'{n} aumentado em {num:.0f}% é {moeda.aumentar(n, num)}.')
print(f'{n} diminuído em {num:.0f}% é {moeda.diminuir(n, num)}')

