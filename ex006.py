# Crie um algoritmo que leia um número, seja ele inteiro ou decimal e mostre seu dobro, triplo,
# raiz quadrada e raiz cúbica.
n = int(input('\033[36mDigite um número qualquer: \033[m'))
n1 = n * 2
n2 = n * 3
n3 = n ** (1/2)
n4 = n ** (1/3)
print('O dobro de {} é {}.'.format(n, n1))
print('O triplo de {} é {}.'.format(n, n2))
print('A raiz quadrada de {} é {:.2f}. \nA raiz cúbica de {} é {:.2f}.'.format(n, n3, n, n4))

# Ou
s = int(input('Digite um número: '))
print('O dobro de {} é {}.'.format(s, s*2))
print('O triplo de {} é {}.'.format(s, s*3))
print('A raiz quadrada de {} é {:.2f}.'.format(s, pow(s, (1/2))))
print('A raiz cúbica de {} é {:.2f}.'.format(s, pow(s, (1/3))))
# 'pow' pode ser usado para calcular raízes.

