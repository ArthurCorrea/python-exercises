# Crie um programa que leia um ângulo qualquer e mostre seu seno, cosseno e tangente.
from math import radians, sin, cos, tan
n = float(input('Valor do ângulo: '))
print(f'O ângulo de {n}° tem o seno de {sin(radians(n)):.2f}.')
print(f'O ângulo de {n}° tem o cosseno de {cos(radians(n)):.2f}.')
print(f'O ângulo de {n}° tem a tangente de {tan(radians(n)):.2f}.')


