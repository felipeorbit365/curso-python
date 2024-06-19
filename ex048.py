soma = 0
contador_valores = 0

for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma = soma + numero
        contador_valores = contador_valores + 1 
print(f'A soma de todos os {contador_valores} valores solicitados é {soma}')

'''
Para encontrar os múltiplos de 3, é necessário verificar se o número é divisível por 3, ou seja, com resto de divisão 0.

Nesse caso, não pode começar do 3 na contagem, pois o 1 é ímpar e relevante para a questão do exercício. 
Começando do 1 e o salto sendo de 2 em 2, os números ímpares são obtidos -> 1, 3, 5, 7...
Nessa resolução, o contador começa a contar do número 1 e pula de 2 em 2 (considerando apenas os ímpares). 
É verificado se cada número ímpar é múltiplo de 3. Começa com todos os números ímpares e verifica se são múltiplos de 3.

Verifique a resolução alternativa abaixo: 

soma = 0
contador_valores = 0

for numero in range(3, 501, 3):
    if numero % 2 == 1:
        soma = soma + numero
        contador_valores = contador_valores + 1
print(f'A soma de todos os {contador_valores} valores solicitados é {soma}')

Desse modo, que também é correto, o contador começa a contar a partir do número 3.
Considera-se apenas os múltiplos de 3 e depois verifica quais deles são ímpares. 


Diferença:

O 1º considera os números ímpares primeiro e em seguida verifica se são múltiplos de 3. 
O 2º considera os múltiplos de 3 primeiro e em seguida faz a análise se são ímpares ou não. 

Também existem duas formas de representar:

    soma = soma + numero ------------> soma += numero (recebe ele mesmo mais o número em questão)
    contador_valores = contador_valores + 1 ------------> contador_valores += 1 (recebe ele mesmo mais 1)
'''