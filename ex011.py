# Crie um programa que calcule a altura e a largura de uma parede e diga quantos
# litros de tinta são necessários para pintá-la,  considerando que cada litro pinta 2m².
n = float(input('Largura da parede: '))
q = float(input('Altura da parede: '))
area = n * q
print(f'Essa parede tem as dimensões {n}m x {q}m, totalizando {area}m².')
print(f'Portanto, serão necessários {area/2} litros de tinta para pintá-la!')
