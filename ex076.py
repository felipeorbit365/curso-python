listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}') # Aspas duplas para não afetar a impressão do F-String com 40 espaços centralizados
print('-' * 40)
for posicao in range(0, len(listagem)): # O range começa do 0 e com o len() contempla o tamanho inteiro da lista
    if posicao % 2 == 0: # Analisa a posição de cada elemento da tupla. Os itens estão em posições pares e os valores estão em posições ímpares
        print(f'{listagem[posicao]:.<30}', end='') # Exibe os itens, já que são pares, alinha o texto à direita completando com pontinhos
    else: # Aí já sabe que são os preços dos produtos
        print(f'R${listagem[posicao]:>7.2f}') # Exibe os prdutos, já que são ímpares, alinha o texto e formata a casa decimal
print('-' * 40)

""""
print(listagem[posicao]) 
Imprime o elemento da tupla na posição correspondente ao valor atual no índice
"""
