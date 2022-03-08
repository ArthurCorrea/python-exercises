# Crie um programa que tenha um tupla totalmente preenchida com
# uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20)
# e mostrá-lo por extenso.
números = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número \033[1;30m{números[n]}\033[m.')
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resposta == 'N':
            print('\033[1;31mPROGRAMA ENCERRADO!\033[m')
            break

