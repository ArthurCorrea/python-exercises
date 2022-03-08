# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo
# agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma possibilidade.


def p():
    print('-' * 32)


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Por favor digite somente números inteiros válidos.\033[m')
        if ok:
            break
    return valor


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except:
            print('\033[1;31mERRO! Digite um número real válido.\033[m')
            continue
        else:
            return n


p()
n = leiaInt('Digite um número inteiro: ')
num = leiaFloat('Digite um número real: ')
p()
print(f'Você digitou os números {n} e {num}!')
p()
