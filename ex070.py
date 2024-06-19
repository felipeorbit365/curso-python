total_compra = 0
produto_barato = ' '
menor_preco = 0
produtos_caros = 0

print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)

while True: 
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total_compra = total_compra + preco
    if menor_preco == 0 or preco < menor_preco: # É necessário inicializar no 0 
        menor_preco = preco
        produto_barato = produto
    if preco > 1000:
        produtos_caros = produtos_caros + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('------ FIM DO PROGRAMA -----')
print(f'O total da compra foi R${total_compra:.2f}')
print(f'Temos {produtos_caros} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produto_barato} e custa R${menor_preco:.2f}')

'''
Solução do Guanabara para descobrir o menor valor:

contador = 0

while True:
contador = contador + 1

if contador == 1: 
    menor_valor = valor
else: 
    if valor < menor_valor:
    menor_valor = valor

Desse modo, usando o contador, o primeiro valor inserido é inicializado como o menor
Ao contador for passando, o primeiro if não é mais verdadeiro, caindo no else
O else faz com que, se o valor da vez for menor que o último menor valor armazenado,
o valor da vez se torna o menor valor. 

Outra solução do Guanabara (a melhor dele):

contador = 0

while True:
contador = contador + 1

if contador == 1 or valor < menor_valor:
    menor_valor = valor

Assim, ele declara o menor valor com o primeiro valor declarado.
A mudança é feita de acordo com o avanço dos contadores com a inclusão de outros produtos.

or -> Precisa de apenas uma premissa verdadeira. Se for o primeiro bloco, OU o segundo. 
Tendo uma premissa verdadeira, o bloco é executado.
---

Minha solução:
menor_valor é inicializado como 0, então a condicional 'if menor_valor == 0 or valor < menor_valor'
verifica se menor_valor é igual a 0 ou se o valor atual é menor que o menor_valor
Se qualquer uma dessas condições for verdadeira, ele atualiza menor_valor para o valor atual 
e também atualiza produto_barato para o produto correspondente.

menor_valor == 0: Se o menor_valor ainda não foi atualizado (inicializado como 0), então este é o menor preço encontrado até agora.
or: Uma vez que or é uma operação de curto-circuito, se a primeira parte da condição (menor_valor == 0) for verdadeira, 
a segunda parte não será avaliada. Portanto, se o menor valor for 0, não precisamos verificar a segunda parte da condição.
valor < menor_valor: Se o preço atual for menor do que o menor valor registrado até agora, então atualizamos menor_valor com o valor atual.

'''