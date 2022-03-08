# Desenvolva um programa onde o usuário digite um expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados na ordem correta.
expressão = str(input('Digite sua expressão: '))
paren = list()
for simb in expressão:
    if simb == '(':
        paren.append('(')
    elif simb == ')':
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(')')
            break
if len(paren) == 0:
    print('Sua expressão é válida.')
else:
    print('Sua expressão está inválida.')
