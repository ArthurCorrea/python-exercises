# Desenvolva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
vl = int(input('A que velocidade seu carro estava: '))
multa = (vl - 80) * 7
if vl > 80:
    print('Você estava acima do limite permitido, portando, você receberá uma multa!')
    print(f'Sua multa será de R${multa},00!')
else:
    print('Ótimo! Você estava abaixo do limite, pode seguir seu caminho!')

