# Crie um tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) apenas os 5 primeiros colocados;
# B) os últimos 4 colocados da tabela;
# C) uma lista com os times em ordem alfabética;
# D) em que posição está o time da Chapecoense.
tabela = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio',
          'Atlético-PR', 'São Paulo', 'Internacional', 'Corintians',
          'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama',
          'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará',
          'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')

print('==' * 40)
print('COLOCAÇÃO: ')
for t in tabela:
    print(f'{t}', '- ', end='')
print('←')
print('==' * 40)
print(f'5 primeiros colocados: {tabela[0:5]}')
print('==' * 40)
print(f'Últimos 4 colocados: {tabela[-4:]}')
print('==' * 40)
print(f'Lista dos times em ordem alfabética: {sorted(tabela)}')
print('==' * 40)
print(f'A Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição.')
print('==' * 40)
