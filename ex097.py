# Desenvolva um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem
# com tamanho adaptável.
# Ex: escreva('Olá, Mundo!')
# Saída: -------------
#         Olá, Mundo!
#        -------------


def escreva(msg):
    for c in range(0, len(msg)):
        print('-', end='')
    print(f'\n{msg}')
    for c in range(0, len(msg)):
        print('-', end='')
    print()


# Programa Principal
escreva('Olá, como vai você?')
escreva('Eu vou bem, obrigado! E você, como está?')
escreva('Estou bem!')
escreva('Esse programa é bem legal. Independente do tamanho da frase, os traços irão acompanhar!')

# Resolução do professor


def escrevan(msg):
    tam = len(msg) + 4
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)


escrevan('Oi')
escrevan('Esse tipo de programa também é muito bacana!')
escrevan('Além dos traços acompanharem as frases, fica uma bordinha boniitnho no início e no final!')
