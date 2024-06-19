matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_colunas = 0
soma_pares = 0
maior_valor = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: ')) # Coloca de acordo com a linha e coluna
print('-' * 50)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='') 
        if matriz[linha][coluna] % 2 == 0:
            soma_pares = soma_pares + matriz[linha][coluna]
    print() 

for linha in range(0, 3): # A coluna é fixa como 2, então deve percorrer as linhas
    # A 3 ª coluna é fixa, ou seja, 2. Por isso, precisa percorrer as linhas
    soma_colunas = soma_colunas + matriz[linha][2] # A coluna já é fixada no 2 (3ª coluna), o que varia é a linha

for coluna in range(0, 3): # A linha está sempre fixa (2ª linha), então é preciso percorrer as colunas
    if coluna == 0: # Inicializa para fazer a comparação de acordo com a 1ª coluna, já que é o 1º valor fornecido
        maior_valor = matriz[1][coluna]
    elif matriz[1][coluna] > maior_valor:
        maior_valor = matriz[1][coluna]
        
print('-' * 50)
print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da 3ª coluna é {soma_colunas}')
print(f'O maior valor da 2ª linha é {maior_valor}')
