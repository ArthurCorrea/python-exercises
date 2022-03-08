# Crie um programa onde o usuário possa digitar cinco valores
# númericos e cadastre-os numa lista, já na posição correta de inserção.
# (sem usar o sort()).
# No final, mostre a lista ordenada na tela.
lista = []
for c in range(1, 6):
    n = int(input(f'Digite o {c}° valor: '))
    if c == 1:
        lista.append(n)
        print('Valor adicionado no início da lista.')
    elif n > lista[-1]:
        lista.append(n)
        print('Valor adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos} da lista.')
                break
            pos += 1

print(f'Lista: {lista}')
