# Desenvolva um programa que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com
# a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso;
# - Entre 18.5 e 25: Peso ideal;
# - 25 até 30: Sobrepeso;
# - 30 até 40: Obesidadade;
# - Acima de 40: Obesidade mórbida.
print('\033[36m-=-\033[m' * 7)
print('\033[36mCalculdora de IMC\033[m')
print('\033[36m-=-\033[m' * 7)

massa = float(input('\033[31mDigite sua massa: \033[m'))
altura = float(input('\033[35mDigite sua altura: \033[m'))

imc = massa / (altura*altura)

if imc < 18.5:
    print(f'Seu IMC é {imc:.1f}. Você está abaixo do peso.')
elif 18.5 <= imc < 25.0:
    print(f'Seu IMC é {imc:.1f}. Você está no peso ideial.')
elif 25.0 <= imc < 30.0:
    print(f'Seu IMC é {imc:.1f}. Você está com o peso elevado.')
elif 30.0 <= imc < 40.0:
    print(f'Seu IMC é {imc:.1f}. Você está obeso.')
else:
    print(f'Seu IMC é {imc:.1f}. Você tem obesidade mórbida.')




