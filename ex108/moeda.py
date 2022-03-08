def dobro(n):
    num = n * 2
    return num


def metade(n):
    num = n / 2
    return num


def aumentar(n, aumenta):
    num = (n * aumenta) / 100
    num += n
    return num


def diminuir(n, diminui):
    nu = n
    nume = (nu * diminui) / 100
    num = n - nume
    return num


def moeda(n, cifrao='R$'):
    return f'{cifrao}{n:.2f}'.replace('.', ',')
