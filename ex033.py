primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))

if primeiro > segundo and primeiro > terceiro:
    maior = primeiro

if segundo > primeiro and segundo > terceiro:
    maior = segundo

if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

if primeiro < segundo and primeiro < terceiro:
    menor = primeiro

if segundo < primeiro and segundo < terceiro:
    menor = segundo

if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))

"""
Seria possível declarar um menor/maior valor por conta própria, diretamente, sem testar.
Isso reduz a utilização de um if.
Sempre é uma boa ideia testar todas as posições nesse tipo de caso, para ver se realmente indica corretamente.
Exemplo:
maior = a
if b > a and b > c:
maior = B
if c > a and c > b:
maior = c
O mesmo vale para o maior.

Também é essencial saber identidicar o que está dentro e fora do if.
O que está fora do if sempre é executado. Na condicional, apenas se corresponder.
"""
