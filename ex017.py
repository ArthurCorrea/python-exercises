# Desenvolva um algoritmo que leia o comprimento do cateto oposto e do cateto adjacente
# e calcule a hipotenusa desse triângulo retângulo.
import math
catopos = float(input('Comprimento do cateto oposto: '))
catadja = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catopos, catadja)
print(f'A hipotenusa desse triângulo retângulo vale {hipotenusa}!')

# Ou
catoposto = float(input('Comprimento do cateto oposto: '))
catadjacente = float(input('Comprimento do cateto adjacente: '))
h = catoposto ** 2 + catadjacente ** 2
hipot = h ** (1/2)
print(f'A hipotenusa desse triângulo retângulo vale {hipot:.2f}!')

