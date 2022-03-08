# Crie um programa que leia uma frase qualquer e mostre:
# -> Quantas vezes aparece a letra "a";
# -> Em que posição ela aparece primeiro;
# -> Em que posição ela aparece por último.
frase = str(input('Digite uma frase: ')).strip()
vezes = frase.upper()
print('A letra "A" em aparece {} vezes.'.format(vezes.count('A')))
print('Ela aparece pela primeira vez na posição {}.'.format(vezes.find('A')+1))
print('Ela aparece pela última vez na posição {}.'.format(vezes.rfind('A')+1))





