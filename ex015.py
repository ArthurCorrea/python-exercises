# Crie um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por Km rodado.
n = int(input('Durante quantos dias o carro foi alugado? '))
q = float(input('Quantos Km foram percorridos? '))
print(f'O preço a pagar é de R${(n * 60) + (q * 0.15):.2f}!')

