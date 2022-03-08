# A CNN precisa de um programa que leia o ano de nascimento
# de um atleta e mostre a sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - ATÉ 20 ANOS: SÊNIOR
# - Acima: MASTER
from datetime import date
print('\033[36mBem-vindo à sua inscrição na CNN!\033[m')
ano = int(input('\033[31mPor favor, diga o seu ano de nascimento:\033[m '))
anoatual = date.today().year
idade = anoatual - ano
if idade <= 9:
    print(f'Você tem {idade} anos.\nVocê está na categoria MIRIM.')
elif idade <= 14:
    print(f'Você tem {idade} anos.\nVocê está na categoria INFANTIL.')
elif idade <= 19:
    print(f'Você tem {idade} anos.\nVocê está na categoria JÚNIOR.')
elif idade <= 25:
    print(f'Você tem {idade} anos.\nVocê está na categoria SÊNIOR.')
else:
    print(f'Você tem {idade} anos.\nVocê está na categoria MASTER.')
print('\033[35mPor favor, dirija-se para a sala à esquerda.\033[m')



