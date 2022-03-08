# Escreva um programa que pergunte o salário de um funcionário e calcule o
# valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para salários inferiores ou iguais, o aumento é de 15%.
salário = float(input('Qual o seu salário? '))
maior = salário * 10 / 100 + salário
menor = salário * 15 / 100 + salário
if salário > 1250.0:
    print(f'Ok! Você recebeu um aumento de 10%, agora seu salário é R${maior}!')
else:
    print(f'Ótimo! Você recebeu um aumento de 15%, agora seu salário é R${menor}!')


