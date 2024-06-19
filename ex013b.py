produto = float(input('Preço do produto: R$'))
pagamento = input('O pagamento será parcelado ou à vista? ')

if pagamento == 'Parcelado':
    valor_novo = produto + (produto * 8/100)
    print('Parcelado, o produto de R${:.2f} tem 8% de juros e passa a custar R${:.2f}'.format(produto, valor_novo))

elif pagamento == 'À vista':
    valor_novo = produto - (produto * 10/100)
    print('À vista, o produto de R${:.2f} tem 10% de desconto e passa a custar R${:.2f}'.format(produto, valor_novo))

else:
    print('Sua forma de pagamento não é válida. Tente novamente.')
