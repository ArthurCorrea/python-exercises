# Desenvolva um programa que mostre o valor do produto e em seguida seu novo preço
# com 5% de desconto.
n = float(input('Quanto custa esse produto? R$'))
des = (n * 5) / 100
preço = n - des
print(f'O produto que custa R${n:.2f}, com 5% de desconto, custará R${preço:.2f}!')

# Desenvolva um programa que mostre o valor do produto, o valor do desconto escolhido
# e seu novo preço.
q = float(input('Quanto custa esse produto? R$'))
s = float(input('Quantos % esse produto tem de desconto? '))
d = (q * s) / 100
pç = q - d
print(f'O produto que custa R${q:.2f}, com {s:.0f}% de desconto, custará {pç:.2f}!')
