valores = []

for contador in range(0, 5): 
    valor = int(input('Digite um valor: '))
    if contador == 0 or valor > valores[-1]: # Se for o 1º valor ou se o número lido for maior que o último elemento
        valores.append(valor) # Adiciona à lista
    else: # Tem que descobrir em que posição vai inserir
        posicao = 0 # Varre o vetor inteiro desde o começo
        while posicao < len(valores): # Vai da posição 0 até a última posição 
            if valor <= valores[posicao]: # Verifica dentro de cada posição se o número a ser inserido é menor ou igual a ele 
                valores.insert(posicao, valor) # Se for menor ou igual, é inserido numa posição específica
                break # Na posição da vez, é inserido o valor e quebra o laço
            posicao = posicao + 1 # A posição vai passando para a próxima posição
print('-' * 30)
print(f'Os valores digitados em ordem foram: {valores}')

# Os valores são lidos e analisados se são colocados no início, meio ou fim
# Se é o 1º ou maior que o último, são adicionados
# Se não for o 1º, nem maior que o último, fica em outra posição 
# As posições são lidas de acordo com o andamento da lista

'''
Lógica do if/or de forma mais básica: 
  if contador == 0: 
        valores.append(valor) # Se for o 1º valor, simplesmente adiciona
    elif valor > valores[len(valores)-1]: # Analisa o número de elementos e pega o último 
        valores.append(valor) # Se for maior que o último, adiciona
'''