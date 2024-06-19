import random
numeros_sorteados = (random.randint(1, 10), random.randint(1,10),
                      random.randint(1,10), random.randint(1, 10),
                      random.randint(1, 10))
print(f'Os valores sorteados foram: {numeros_sorteados}')
print(f'O maior valor sorteado foi: {max(numeros_sorteados)}')
print(f'O menor valor sorteado foi: {min(numeros_sorteados)}')
