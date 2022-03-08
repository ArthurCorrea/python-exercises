# Desenvolva um programa que gerencie o aproveitamento de um
# jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de
# gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos
# durante o campeonato.
nome = str(input('Nome: ')).strip()
partidas = int(input('Partidas jogadas nesse campeonato: '))
total = {'Nome': nome, 'Partidas': partidas}
gol = list()
for c in range(0, partidas):
    gols = int(input(f'--> Gols na partida {c + 1}° partida: '))
    gol.append(gols)
total['Gols'] = gol
total['Total de gols'] = sum(gol)

print('-='*40)

for k, i in total.items():  # 1° forma
    print(f'-> {k}: {i}')

print('-='*40)

print(total)     # 2° forma

print('-='*40)


# 3° forma
print(f'O jogador {total["Nome"]} jogou {total["Partidas"]} partidas.')
i = 0
while i < partidas:
    print(f'--> Na {i + 1}ª partida fez {total["Gols"][i]} gols.')
    i += 1
print(f'Fez um total de {total["Total de gols"]} gols.')
print('-='*40)
