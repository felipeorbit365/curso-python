from random import randint
from time import sleep

numeros_sorteados = []
jogos = [] # Lista para armazenar os sorteios

print('-' * 20)
print('JOGO DA MEGA-SENA')
print('-' * 20)
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
total_jogos =  1 # 1 pois começa com 1 jogo, se fosse 0, o while faria 1 jogo a mais que o desejado

while total_jogos <= quantidade_jogos:
    contador = 0
    while True:
        numero = randint(1, 60)
        # Se o número aleatório não estiver entre os números sorteados, ele é adicionado à lista
        if numero not in numeros_sorteados:
            numeros_sorteados.append(numero)
            contador = contador + 1
        if contador >= 6: # Interrompe o laço se o número de números sorteados for 6
            break
    numeros_sorteados.sort()
    # A cada vez que sortear, faz uma cópia dos números sorteados e apaha a lista
    jogos.append(numeros_sorteados[:])
    numeros_sorteados.clear()
    total_jogos = total_jogos + 1
print(f'--- SORTEANDO {quantidade_jogos} JOGOS ---')

# Percorre cada elemento da lista de jogos indicando o índice 
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1}: {lista}') # Adiciona 1 para que não mostre 'Jogo 0', já que o índice começa em 0
    sleep(1)
print('--- BOA SORTE ---')
# Existe uma lista grande, com todos os jogos, cheia de listas menores guardando todos os palpites
