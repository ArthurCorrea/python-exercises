# Crie um programa que simule o funcionamento de um caixa eletrônica.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro).
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('\033[1;35m=='*20)
print('{:^35}\033[m'.format('ARTHUR BANK'))
print('\033[1;35m==\033[m'*20)

saque = int(input('\033[1;30mQual valor deseja sacar? R$\033[m'))

print('\033[1;30m==\033[m' * 20)

dinheiro = saque
céd = 50
totalcéd = 0

print('\033[1;30mTotal de:\033[m')

while True:

    if dinheiro >= céd:
        dinheiro -= céd
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'\033[1;31m{totalcéd}\033[m \033[1;30mnotas de\033[m \033[1;34mR${céd},00\033[m')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totalcéd = 0

        if dinheiro == 0:
            break

print('\033[1;30m==' * 20)
print('OBRIGADO E VOLTE SEMPRE!\033[m')
print('\033[1;30m==\033[m' * 20)
