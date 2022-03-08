# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando espaços.
# EX: A SACADA DA CASA; A TORRE DA DERROTA; O LOBO AMA O BOLO
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'{junto} de trás pra frente é {inverso}.')
if inverso == junto:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')

