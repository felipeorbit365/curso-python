numeros_digitados = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))
print(f'O valor 9 apareceu {numeros_digitados.count(9)} vez(es)')
if 3 in numeros_digitados: # Analise se o 3 foi digitado ou não e mostra de acordo
    print(f'O valor 3 apareceu na {numeros_digitados.index(3)+1}ª posição') # Adiciona mais um porque o índice começa no 0
else: 
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados são: ', end='')
for numero in numeros_digitados: # Percorre os valores
    if numero % 2 == 0: 
        print(numero, end=' ')

'''
Não é possível calcular o módulo de uma tupla, por isso esse método é realizado assim

De tal modo, 'for numero in numero_digitados' percorre todos os elementos da tupla e faz a verificação no if para indicar os pares
'''