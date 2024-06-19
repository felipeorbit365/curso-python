numero = int(input('Digite um número para saber a tabuada: '))

for contador in range(1, 11):
    print(f'{numero} x {contador} = {numero * contador}')

'''
Está correto, mas não é tão prático:

numero = int(input('Digite um número para saber a tabuada: '))

for c in range(1, 11):
    resultado = numero * c
    print(numero, end='')
    print (' x ', end='')
    print(c, end='')
    print(' = ', end='')
    print(resultado)
'''