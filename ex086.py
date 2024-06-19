matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Uma lista para cada linha com três valores
# A lista matriz tem três listas dentro e dentro de cada lista vai haver três valores
# Os zeros são substituídos pelo valor informado pelo usuário
# Cada lista é uma linha da matriz
# Um laço dentro do outro para suprir todas as linhas e colunas
# Alimenta os números nas posições
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: ')) # Coloca de acordo com a linha e coluna
print('-' * 50)

# Estrutura a matriz na tela
for linha in range(0, 3):
    for coluna in range(0, 3):
        # :^5 -> Faz ficar em 5 espaços centralizados
        print(f'[{matriz[linha][coluna]:^5}]', end='') # Deixa um valor ao lado do outro
    print() # Quebra a linha toda vez a repetição completa todas as colunas da linha
