valores = [[],[]] # Uma lista única com duas listas internas
numero_usuario = 0

for contador in range(1, 8):
    # Não lê o valor diretamente com .append(), pois serão separados em sub-listas
    numero_usuario = int(input(f'Digite o {contador}º valor: '))
    if numero_usuario % 2 == 0:
        valores[0].append(numero_usuario) # Adiciona no índice 0 da lista, a 1ª sub-lista
    else:
        valores[1].append(numero_usuario) # Adiciona no índice 1 da lista, a 2ª sub-lista
print('=' * 50)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')

'''
Utilizando duas novas listas (não da forma como o Guanabara queria):

lista_valores = []
valores_pares = []
valores_impares = []

for contador in range(1, 8):
    lista_valores.append(int(input(f'Digite o {contador}º valor: ')))

lista_valores.sort()

for valor in lista_valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)

print('=' * 50)
print(f'Os valores pares digitados foram: {valores_pares}')
print(f'Os valores ímpares digitados foram: {valores_impares}')

---

Comentário interessante do YouTube:

Uma coisa que eu percebi nos comentarios é que pouca gente pensou em atribuir uma operação ao indice da lista.
Se colocamos a sub lista dos valores pares no indice 0 da lista principal e os valores impares na sub lista do indice 1, repare que bate com os valores do resto da divisão, um par qualquer vai dar resto = 0 e um impar qualquer resto = 1, então podemos ao invés de dar um valor fixo ao indice que o programa vai acessar da lista para adicionar o numero, colocar a propia operação de resto da divisão por 2.
Em código fica assim (considerando que os numeros foram armazenados na lista valores, c é o contador dentro do for e numero é o valor que o usuario acaba de digitar.

valores = [[], []] 
for c in range(1,8):
    numero= int(input(f'Numero {c}°'))
    valores[numero % 2].append(numero)

combinando com a função sorted, podemos ordenar os valores nas listas dentro da propia função print, isso significa que da para fazer o exercicio inteiro em 6 linhas, abaixo ele inteiro:

valores = [[], []] 
for c in range(1,8):
    numero= int(input(f'Numero {c}°'))
    valores[numero % 2].append(numero)
print(f'Valores pares digitados: {sorted(valores[0])}')
print(f'Valores impares digitados: {sorted(valores[1])}')
'''