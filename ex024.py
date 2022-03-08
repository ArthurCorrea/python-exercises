# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não
# com a palavra "Santo"
name = str(input('Em qual cidade você mora? ')).strip()
print(name[:5].lower() == 'santo')


