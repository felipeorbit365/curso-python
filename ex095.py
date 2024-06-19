time = []
jogador = {}
gols_partidas = []

while True:
    jogador.clear() # Limpa a cada laço os dados de jogador, pois estará sendo outro a cada repetição, antes da leitura
    jogador['nome'] = str(input('Nome do Jogador: '))
    quantidade_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols_partidas.clear() # Precisa esvaziar os gols das partidas para separar de acordo com cada jogador, antes da leitura
    for contador in range(0, quantidade_partidas):
        gols_partidas.append(int(input(f'Quantos gols na partida {contador+1}? ')))
    jogador['gols'] = gols_partidas[:] 
    jogador['total de gols'] = sum(gols_partidas)
    time.append(jogador.copy()) # Faz a cópia de jogador na lista time
    while True:
        resposta_usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta_usuario in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta_usuario == 'N':
        break

# Estilizando a estrutura apenas, o cabeçalho
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys(): # Para cada elemento, mostrar as chaves
    print(f'{i:<15}', end='')
print()

print('-' * 40)
# K -> Key (Código) | V -> Valor (Jogador) | D -> Dado (cada dado do jogador -> gols e total de gols)
for k, v in enumerate(time): # Percorre cada jogador da lista time
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print() # Quebra a linha depois de mostrar tudo
print('-' * 40)

while True:
    escolha_jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if escolha_jogador == 999:
        break
    # Se a escolha do usuário for referente ao código de um jogador que não existe, dá erro
    if escolha_jogador >= len(time): # Se a escolha for maior que o time, obtido por len(), erro
        print(f'ERRO! Não existe jogador com código {escolha_jogador}')
    else: # Se estiver dentro do limite
        print(f'- LEVANTAMENTO DO JOGADOR {time[escolha_jogador]["nome"]}: ')
        # Para encontrar o nome do jogador -> time[escolha_jogador]["nome"]
        # Na lista time, acessa o desejado com o índice númerico de [escolha_jogador], onde é possível acessar o nome através do dicionário
        for i, g in enumerate(time[escolha_jogador]['gols']): # Mostra a quantidade gols a cada partida
            # I -> índice (partida) | G -> Gols | Utiliza-se enumerate() pois são itens de
            print(f'No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print('--- VOLTE SEMPRE ---')
