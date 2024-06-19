# Solução do Bard/Gemini
from random import randint
from time import sleep

# Define o número máximo de jogos
numero_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

# Exibe o cabeçalho
print('-' * 20)
print('JOGO DA MEGA-SENA')
print('-' * 20)

# Exibe a mensagem de sorteio
print(f'--- SORTEANDO {numero_jogos} JOGOS ---')

# Lista para armazenar os jogos
jogos = []

# Loop para gerar os jogos
for _ in range(numero_jogos):

    # Cria uma lista vazia para armazenar os números do jogo
    numeros = []

    # Loop para gerar os 6 números do jogo
    for _ in range(6):

        # Gera um número aleatório entre 1 e 60
        sorteio = randint(1, 60)

        # Verifica se o número já está na lista
        while sorteio in numeros:

            # Gera outro número aleatório
            sorteio = randint(1, 60)

        # Adiciona o número à lista do jogo
        numeros.append(sorteio)

    # Cria uma nova lista para armazenar os números ordenados
    numeros_ordenados = sorted(numeros)

    # Adiciona o jogo à lista de jogos
    jogos.append(numeros_ordenados)

# Loop para mostrar os jogos
for contador, jogo in enumerate(jogos, 1):

    # Exibe o jogo
    print(f'Jogo {contador}: {jogo}')

    # Aguarda um segundo
    sleep(1)

# Exibe a mensagem de despedida
print('--- BOA SORTE! ---')
