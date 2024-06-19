numero = int(input('Digite um número para calcular seu fatorial: '))
contador = numero
fatorial = 1 
print(f'Calculando {numero}! -> ', end='')

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='') 
    fatorial = fatorial * contador
    contador = contador - 1 
print(f'{fatorial}')

"""
from math import factorial também é uma opção

fatorial = 1 # Fator nulo de multiplicação é 1. Deixa a multiplicação limpa. De adição e subtração é 0

print(' x ' if contador > 1 else ' = ', end='') # Estiliza o x ao lado dos números enquanto for maior que 1 (que é onde deve chegar) e finaliza com o =

contador = contador - 1 # Tira 1 do Contador por vez

Forma de calcular fatorial: 

numero = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1
while numero > 0:
    fatorial = fatorial * numero
    numero = numero - 1
print(fatorial)

Utilizando for:

numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1

for contador in range(1, numero + 1):
    fatorial = fatorial * contador

print(f'O fatorial de {numero} é {fatorial}')

Utilizando for no estilo Guanabara:

numero = int(input('Digite um número para calcular seu fatorial: '))
fatorial = 1
print(f'Calculando {numero}! -> ', end='')

for contador in range(numero, 0, -1):
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='') 
    fatorial *= contador

print(f'{fatorial}')

"""