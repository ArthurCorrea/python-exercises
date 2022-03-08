# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento
# de cada jogador.
j = dict()
jogadores = list()
listagols = list()

while True:
    j.clear()
    j['Nome'] = str(input('Nome: ')).strip()
    partidas = int(input('Partidas jogadas no campeonato: '))
    listagols.clear()
    for p in range(0, partidas):
        listagols.append(int(input(f'--> Gols na {p + 1}ª partida: ')))
    j['Gols'] = listagols[:]
    j['Total de gols'] = sum(listagols)
    jogadores.append(j.copy())
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break
print('-='*20)

print('N°', end='')
for i in j.keys():
    print(f'{i:^10} ', end=' ')
print()
print('-='*20)

for k, i, in enumerate(jogadores):
    print(f'{k:<3}', end='')
    for d in i.values():
        print(f'{str(d):^10} ', end='')
    print()
print('-='*20)

while True:
    resp = int(input('Deseja acessar o aproveitamento de qual jogador? [999 para parar] '))
    if resp == 999:
        print(f'{"PROGRAMA ENCERRADO!":^10}')
        break
    if resp > len(jogadores):
        print(f'ERRO! O jogador com número {resp} não existe.')
    else:
        print(f'-- Aproveitamento do jogador {jogadores[resp]["Nome"]} --')
        for i, g in enumerate(jogadores[resp]["Gols"]):
            print(f'Gols feitos no {i+1}° jogo: {g}')
    print('-='*20)
