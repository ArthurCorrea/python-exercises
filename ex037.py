# Escreva um programa que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário;
# 2 para octal;
# 3 para hexadecimal.
n = int(input('Digite um número: '))
print('''Base de conversão: 
(1) - Sistema binário
(2) - Sistema octal
(3) - Sistema hexadecimal''')
escolha = int(input('Escolha: '))
if escolha == 1:
    print(f'O número {n} convertido para BINÁRIO é {bin(n)[2:]}.')
elif escolha == 2:
    print(f'O número {n} convertido para OCTAL é {oct(n)[2:]}.')
elif escolha == 3:
    print(f'O número {n} convertido para HEXADECIMAL é {hex(n)[2:]}.')
else:
    print('Por favor, reinicie o programa.')
