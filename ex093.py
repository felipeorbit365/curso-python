jogador = {}
gols_partidas = []
total_gols = 0

jogador['nome'] = str(input('Nome do Jogador: '))
quantidade_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for contador in range(0, quantidade_partidas):
    gols_partidas.append(int(input(f'Quantos gols na partida {contador}? ')))
jogador['gols'] = gols_partidas[:] # Gera uma cópia dos gols

for gol in gols_partidas:
    total_gols = total_gols + gol
jogador['total de gols'] = total_gols 
# Poderia ser jogador['total de gols'] = sum(gols_partidas)

print('-' * 60)
print(jogador)
print('-' * 60)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-' * 60)
print(f'O jogador {jogador["nome"]} jogou {quantidade_partidas} partidas')
# Poderia ser {len(jogador["gols"])} no lugar de {quantidade_partidas}

for i, v in enumerate(gols_partidas): # Poderia ser enumerate(jogador['gols'])
    print(f'Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total de gols"]} gols.')
