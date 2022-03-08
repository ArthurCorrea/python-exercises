# Desenvolva um programa onde o usuário possa digitar vários valores
# númericos e cadastre-os numa lista. Caso o número já exista lá dentro,
# ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.
valores = []
while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado, será excluído da lista.')

    print('-=' * 20)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-=' * 20)
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break

valores.sort()
print(f'Lista: {valores}')
