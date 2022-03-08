# Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão utilizando
# a estrutura while.
pa = int(input('Primeiro termo da PA: '))
razão = int(input('Razão: '))
décimo = pa
contador = 1
while contador <= 10:
    print(f'{décimo} -> ', end='')
    décimo += razão
    contador += 1
print('FIM!')

