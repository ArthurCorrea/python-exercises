# Crie um programa que leia vários números inteiros pelo teclado. O programa
# só vai parar quando o usuário digitar o valor 999, que é a condição de
# parada. No final, mostre quantos números foram digitados e qual foi
# a soma entre eles (desconsiderando o 999).
n = 0
soma = 0
contador = 0
while n != 999:
    n = int(input('Digite um número [999 para encerrar]: '))
    if n != 999:
        soma += n
        contador += 1

print(f'Foram digitados {contador} valores.')
print(f'A soma entre todos esses valores, exceto o 999, é {soma}.')
