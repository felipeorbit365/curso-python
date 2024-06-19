print('----------------------')
print('SEQUÊNCIA DE FIBONACCI')
print('----------------------')

numero_termos = int(input('Digite a quantidade de termos que deseja exibir: '))

primeiro_termo = 0
segundo_termo = 1
sequencia = 0

print(f'{primeiro_termo} -> ', end='')
print(f'{segundo_termo} -> ', end='')
# Poderia juntar na mesma linha, '{} -> {}'

contador = 3 # Começa do 3 pois os 2 primeiros já são definidos

while contador <= numero_termos:
    sequencia = primeiro_termo + segundo_termo
    print(f'{sequencia} -> ', end='')
    primeiro_termo = segundo_termo
    segundo_termo = sequencia
    contador = contador + 1
print('FIM')

'''
A sequência de Fibonacci é uma sucessão de números inteiros, começando normalmente por 0 e 1, 
na qual cada termo subsequente corresponde à soma dos dois anteriores.
Soma os dois termos anteriores para obter o próximo termo da sequência.
'''