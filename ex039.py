# Faça um programa que leia o ano de nascimento de um jovem e
# informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar;
# - Se já é a hora de se alistar.
# - Se já passou do tempo de alistamento.
# Seu programa também deverá mostrar o prazo que falta ou
# passou do prazo.
from datetime import date

sex = str(input('\033[30mVocê é homem ou mulher?\033[m ')).lower()

if sex == 'homem':
    ano = int(input('\033[30mAno de nascimento:\033[m '))
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 18:
        print(f'Você ainda tem {idade} anos. Falta {18 - idade} ano(s) para você se alistar.')
        print(f'Seu alistamento será em {ano + 18}.')
    elif idade == 18:
        print(f'Com {idade} anos você deve se alistar, jovem!')
    elif idade > 18:
        print(f'Com {idade} anos era para você ter se alistado há {idade - 18} ano(s)!')
        print(f'Seu alistamento foi feito em {ano + 18}.')
else:
    print('\033[36mVocê não precisa se alistar.\033[m')

