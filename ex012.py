preco_produto = float(input('Digite o preço do produto: '))
desconto = preco_produto * 5/100
liquidacao = preco_produto - desconto
print('O produto custava R${:.2f}, com o desconto de 5% passa a custar R${:.2f}'.format(preco_produto, liquidacao))

