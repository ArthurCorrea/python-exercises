# Refaça o desafio 035, acrescentando o recurso de mostrar que
# tipo de triângulo será formado:
# - Equilátero: todos os lados iguais;
# - Isósceles: dois lados iguais;
# - Escaleno: todos os lados diferentes.
n1 = float(input('\033[34mMedida 1:\033[m '))
n2 = float(input('\033[31mMedida 2:\033[m '))
n3 = float(input('\033[36mMedida 3:\033[m '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[30mCom essas medidas É POSSÍVEL montarmos um triângulo!\033[m')
    if n1 == n2 and n2 == n3:
        print('Esse triângulo será EQUILÁTERO.')
    elif n1 == n2 or n1 == n3:
        print('Esse triângulo será ISÓSCELES.')
    elif n1 != n2 and n2 != n3:
        print('Esse triângulo será ESCALENO.')
else:
    print('\033[30mCom essas medidas NÃO É POSSÍVEL montarmos um triângulo!\033[m')

# Forma mais complexa e desnecessária que acabei fazendo
''' if n1 == n2 and n2 == n3 and n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[35mEsse triângulo será EQUILÁTERO!\033[m')
elif n1 == n2 or n1 == n3 and n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[35mEsse triângulo será ISÓSCELES!\033[m')
elif n1 != n2 and n2 != n3 and n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('\033[35mEsse triângulo será ESCALENO!\033[m') '''


