# Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo.
a = float(input('Medida 1: '))
b = float(input('Medida 2: '))
c = float(input('Medida 3: '))

cond1 = b - c < a < b + c
cond2 = a - c < b < a + c
cond3 = a - b < c < a + b

if cond1 & cond2 & cond3:
    print('Com essas medidas É POSSÍVEL montarmos um retângulo.')
else:
    print('Com essas medidas NÃO É POSSÍVEL montarmos um retângulo.')

# Ou
a1 = float(input('Medida 1: '))
b1 = float(input('Medida 2: '))
c1 = float(input('Medida 3: '))

if a1 < b1 + c1 and b1 < a1 + c1 and c1 < a1 + b1:
    print('Com essas medidas É POSSÍVEL montarmos um triângulo.')
else:
    print('Com essas medidas NÃO É POSSÍVEL montarmos um triângulo.')
