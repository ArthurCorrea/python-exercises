# Desenvolva um programa que mostre o salário de um funcionário e em seguida
# mostre quanto ele passará a ganhar após um aumento de 15%.
n = float(input('Qual o salário do funcionário? R$'))
print(f'O funcionário que ganhava R${n:.2f}, com 15% de aumento, passará a ganhar R${n + (n * 15 / 100):.2f}!')

