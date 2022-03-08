# Crie um programa que leia um número qualquer e mostre seu sucessor e antecessor.
cores = {'vermelho': '\033[31m',
         'azulclaro': '\033[36m',
         'amarelho': '\033[33m',
         'pretoebranco': '\033[7;30m',
         'verde': '\033[32m',
         'limpa': '\033[m'}
n = int(input('\033[30mDigite um número: \033[m'))
n1 = n + 1
n2 = n - 1
print('Analisando o número {}{}{}, é possível perceber que seu antecessor é o número {}{}{}'.format(cores['amarelho'], n, cores['limpa'], cores['vermelho'], n2, cores['limpa']))
print('e seu sucessor é o número {}{}{}!'.format(cores['verde'], n1, cores['limpa']))

#Ou
s = int(input('Digite um número: '))
print('Analisando o número {}, é possível perceber que seu antecessor é o número {}'.format(s, s-1))
print('e seu sucessor é o número {}!'.format(s+1))

