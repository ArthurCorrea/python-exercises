# Crie um algoritmo que leia um número em metros e converta-o para km, hm, dam, dm, cm e mm.
import time
print('\033[36m---------------- Conversor de medidas ligado! ----------------\033[m')
n = float(input('\033[35mValor em metros: \033[m'))
print('\033[32mAnalisando...\033[m')
time.sleep(2)
print(f'{n} metros é igual a: \n{(n / 1000)}km \n{(n / 100):.2f}hm \n{(n / 10)}dam \n{n * 10} \n{(n * 100)}cm \n{(n * 1000)}mm')

# Desenvolva um programa que leia um número qualquer, define a tipo de medida e converta para
# os respectivos valores.
print('\033[36mConversor de medidas ligado!\033[m')
q = float(input('\033[32mValor: \033[m'))
med = str(input('\033[35mTipo de medida: (km, m, cm, mm)\033[m '))

if med == 'km':
    metro = q * 1000
    cm = q * 100000
    mm = q * 1000000
    print(f'{q}km é igual a: \n{metro}m \n{cm}cm \n{mm}mm')
elif med == 'm':
    quil = q / 1000
    cm = q * 100
    mm = q * 1000
    print(f'{q}m é igual a: \n{quil}km \n{cm}cm \n{mm}mm')
elif med == 'cm':
    quil = q / 100000
    m = q / 100
    mm = q * 10
    print(f'{q}cm é igual a: \n{quil}km \n{m}m \n{mm}mm')
elif med == 'mm':
    quil = q * 1000000
    m = q * 1000
    cm = q * 10
    print(f'{q}mm é igual a: \n{quil}km \n{m}m \n{cm}cm')
