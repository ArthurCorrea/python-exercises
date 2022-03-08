# Desenvolva um algoritmo que leia o dinhero que você possui e diga quantos dólares ou euros
# você consegue comprar.

n = float(input('\033[31mOlá! Quanto dinheiro você tem? R$\033[m'))
dl = n / 5.30
eur = n / 6.10
print(f'Com R${n} você consegue comprar U${dl:.2f} ou €{eur:.2f}!')
