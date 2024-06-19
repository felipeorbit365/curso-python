print('===============')
print('10 TERMOS DA PA')
print('===============')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo_termo = termo + (10 - 1) * razao

for contador in range(termo, decimo_termo + razao, razao):
    print(f'{contador}', end=' -> ')
print('FIM')


'''
Solução alternativa:

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for contador in range(1, 11):
    progressao = termo + (contador - 1) * razao
    print(f'{progressao}', end=' -> ') 
print('FIM')

Outra solução:

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

progressao = termo
for c in range (0, 10):
    print (f'{progressao}')
    progressao = progressao + razao

'''