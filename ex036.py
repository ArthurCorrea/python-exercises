# Escreva um programa para aprovar um empréstimo bancário para a
# compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('\033[36mValor da casa:\033[m R$'))
salário = float(input('\033[31mSalário:\033[m '))
tempo = float(input('\033[30mEm quantos anos pretende pagar?\033[m '))
mensal = (tempo * 12)
prestação = casa / mensal
if prestação > (salário * 30) / 100:
    print(f'O valor da prestação será de R${prestação:.2f}.')
    print('Lamento, mas não será possível realizar o empréstimo.')
else:
    print(f'O valor da prestação será de R${prestação:.2f}.')
    print('Seu empréstimo será concluído com sucesso!')


