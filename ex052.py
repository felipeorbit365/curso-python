numero = int(input('Digite um número: '))
contador = 0 
contador_divisiveis = 0

for contador in range(1, numero + 1):
    print(contador, end=' ')
    if numero % contador == 0: 
        contador_divisiveis = contador_divisiveis + 1

print(f'\nO número {numero} é divisível por {contador_divisiveis} vezes')

if contador_divisiveis > 2:
    print(f'Por isso, o número {numero} NÃO é primo!')
else: 
    print(f'Por isso, o número {numero} é SIM primo!')
