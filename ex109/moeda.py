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
