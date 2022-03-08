# Desenvolva um programa que leia a temperatura em °C e converta para °F e K.
n = float(input('Temperatura em °C: '))
fh = (n * 9/5) + 32
kl = n + 273.15
print(f'{n}°C correspondem a {fh:.1f}°F ou {kl:.1f}K.')

# Crie um programa que leia a temperatura de qualquer tipo e converta para o tipo escolhido.
print('Conversor de temperaturas ligado!')
q = float(input('Temperatura: '))
t = str(input('Tipo: (°C, °F ou K) '))

if t == '°C':
    f = (q * 9/5) + 32
    k = q + 273.15
    print(f'{q}°C correspondem a {f:.2f}°F ou {k:.2f}K.')

elif t == '°F':
    c = (q - 32) * 5/9
    k = (q - 32) * 5/9 + 273.15
    print(f'{q}°F correspondem a {c:.2f}°C ou {k:.2f}K.')

elif t == 'K':
    c = q - 273.15
    f = (q - 273.15) * 9/5 + 32
    print(f'{q}K correspondem a {c:.2f}°C ou {f:.2f}°F.')



