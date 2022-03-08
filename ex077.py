# Crie um programa que tenha uma tupla com várias
# palavras(não usar acentos). Depois disso, você
# deve mostrar, para cada palavra, quais são as suas vogais.
tupla = ('arthur', 'joelma', 'lucas', 'divino',
         'programador', 'estudar', 'python', 'vida',
         'copo', 'geladeira', 'ovo', 'computador')

for c in tupla:
    print(f'\nNa palavra \033[1;30m{c.upper()}\033[m as vogais são: ', end='')
    for letras in c:
        if letras.upper() in 'AEIOU':
            print(letras, end=' ')
