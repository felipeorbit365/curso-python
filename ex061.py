print('===============')
print('10 TERMOS DA PA')
print('===============')

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    contador = contador + 1
print('FIM')

'''
for contador in range(termo, decimo_termo + razao, razao):
    print(f'{contador}', end=' -> ')
print('FIM')
'''
