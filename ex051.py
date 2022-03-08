# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
pa = int(input('Primeiro termo da PA: '))
razão = int(input('Razão: '))
décimo = pa + (10 - 1) * razão      # CALCULA O N-ÉSIMO TERMO
for c in range(pa, décimo + razão, razão):
    print(c, '->', end=' ')
print('FIM')
