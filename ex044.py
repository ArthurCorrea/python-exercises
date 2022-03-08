# Elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condição de
# pagamento:
# - À vista (dinheiro/cheque): 10% de desconto;
# - À vista no cartão: 5% de desconto;
# - Em até 2x no cartão: preço normal;
# - 3x ou mais no cartão: 20% de juros.
print('\033[36m{:=^40}\033[m'.format(' LOJA DO THÚZIN '))

preço = float(input('\033[30mPreço das compras:\033[m R$'))

print('\033[32mDigite 1 para pagamento à vista no diheiro.')
print('Digite 2 para pagamento à vista no cartão.')
print('Digite 3 para pagamento parcelado de 2x no cartão.')
print('Digite 4 para pagamento parcelado de 3x ou mais no cartão.\033[m')

pagamento = int(input('\033[31mForma de pagamento:\033[m '))

if pagamento == 1:
    des = preço - (preço * 10 / 100)
    print('À vista no dinheiro você recebe 10% de desconto,')
    print(f'portando, custará R${des:.2f}!')
elif pagamento == 2:
    des = preço - (preço * 5 / 100)
    print('À vista no cartão você recebe 5% de desconto,')
    print(f'portanto, custará R${des:.2f}!')
elif pagamento == 3:
    print(f'Você deverá pagar duas parcelas de R${preço/2:.2f} sem acréscimo de juros.')
elif pagamento == 4:
    n = int(input('\033[34mEm quantas vezes deseja parcelar?\033[m '))
    aumento = preço + (preço * 20 / 100)
    print(f'{n} parcelas de R${aumento/n:.2f} COM JUROS resultará num total de R${aumento:.2f}!')
else:
    print('Forma de pagamento inválida.')



