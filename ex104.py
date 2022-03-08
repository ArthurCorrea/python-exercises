# Crie um programa que tenha a função leiaInt(), que vai funcionar
# semelhante à função input() do Python, só que fazendo a validação
# para aceitar apenas um valor numérico. EX: n = leiaInt('Digite um número: ')


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Digite somente um número inteiro.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')

