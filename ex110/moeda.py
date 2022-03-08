def dobro(n, formatar=False):
    num = n * 2
    return num if not formatar else moeda(num)


def metade(n, formatar=False):
    num = n / 2
    return num if not formatar else moeda(num)


def aumentar(n, aumenta, formatar=False):
    num = (n * aumenta) / 100
    num += n
    return num if formatar is False else moeda(num)


def diminuir(n, diminui, formatar=False):
    nu = n
    nume = (nu * diminui) / 100
    num = n - nume
    return num if formatar is False else moeda(num)


def moeda(n, cifrao='R$'):
    return f'{cifrao}{n:.2f}'.replace('.', ',')


def resumo(n=0, aumenta=0, diminui=0):
    print('-='*20)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-='*20)
    print(f'\033[1;30mPreço analisado: \t\t{moeda(n)}'
          f'\nDobro do preço:  \t\t{dobro(n, True)}'
          f'\nMetade do preço: \t\t{metade(n, True)}'
          f'\n{aumenta:.0f}% de aumento:  \t\t{aumentar(n, aumenta, True)}'
          f'\n{diminui:.0f}% de redução:  \t\t{diminuir(n, diminui, True)}\033[m')
    print('-='*20)
