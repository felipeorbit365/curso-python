lista_valores = []
lista_pares = []
lista_impares = []

while True:
    numero = int(input('Digite um número: '))
    lista_valores.append(numero)
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 50)
print(f'A lista completa é: {lista_valores}')
print(f'A lista de pares é: {lista_pares}')
print(f'A lista de ímpares é: {lista_impares}')

"""
Solução do Guanabara para pares e ímpares:

for indice, valor in enumerate(lista_valores):
    if valor % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

O laço analisa cada um dos valores e insere na lista respectiva
"""