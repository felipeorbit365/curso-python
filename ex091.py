from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1' : randint(1, 6),
             'jogador2' : randint(1, 6),
             'jogador3' : randint(1, 6),
             'jogador4' : randint(1, 6)}

ranking = [] # O resultado é tratado como uma lista

print('Valores sorteados: ')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

# Isso gera uma lista com várias tuplas. Pega os valores (1) e coloca do maior para o menor.
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-' * 50)
print('--- RANKING DOS JOGADORES ---')
# Como foi gerada uma lista, utiliza-se enumerate()
# Exemplo da lista gerada: [('jogador1', 6), ('jogador2', 5)]
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
# i -> A posição, o índice dos jogadores. 
# Fica 'i+1' para aparecer 1 e não 0, já que o 1º índice é 0 sempre
# v -> Valor, os jogadores
# v[0] -> O nome dos jogadores, já que é o valor no índice 0 (os nomes)
# v[1] -> O número no dado, já que é o valor no índice 1 (os números)

'''
Explicação no YouTube sobre o itemgetter:

from operator import itemgetter
A = {'biscoito':'120 gramas'}

O número dentro do key=itemgetter() serve para definir o valor que você quer dentro do dicionário. 
No caso, se o valor dentro do itemgetter for 1, pegaria '120 gramas'.
Se fosse 0, pegaria 'biscoito'. 

Outro comentário interessante:

Uma forma mais simples de preencher o dict() seria
dado = dict()
for c in range (1,5):
    dado[f"jogador {c}"] = randint(1,6)
'''