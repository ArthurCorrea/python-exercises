# Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais
# termos. O programa encerra quando ele disser que quer mostrar 0 termos.
from time import sleep
print('-=' * 10)
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
termo = primeiro
contador = 1
total = 0
extra = 10
while extra != 0:
    total += extra
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        contador += 1
    print('PAUSA')
    extra = int(input('Quantos termos a mais você deseja adicionar? '))
    print('.', end='')
    sleep(0.4)
    print('.', end='')
    sleep(0.4)
    print('.')
    sleep(0.8)

print(f'Essa progressão foi finalizada com {total} termos.')
print('FIM DO PROGRAMA')


