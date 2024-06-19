print('============ LOJA ============')
preco_compras = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] À vista - Dinheiro / Cheque
[2] À vista - Cartão
[3] 2 parcelas - Cartão
[4] 3 parcelas ou mais - Cartão  
      ''')
opcao = int(input('Digite sua opção: '))

if opcao == 1:
    desconto = preco_compras * 0.1
    total_pagamento = preco_compras - desconto
    print(f'Sua compra de R${preco_compras:.2f} vai custar R${total_pagamento:.2f} no final.')
elif opcao == 2:
    desconto = preco_compras * 0.05
    total_pagamento = preco_compras - desconto
    print(f'Sua compra de R${preco_compras:.2f} vai custar R${total_pagamento:.2f} no final.')
elif opcao == 3: 
    parcelas = preco_compras / 2
    print(f'Sua compra de R${preco_compras} poderá ser paga SEM JUROS em 2 parcelas de R${parcelas}.')
elif opcao == 4: 
    numero_parcelas = int(input('Quantidade de parcelas: '))
    juros = preco_compras * 0.2
    total_pagamento = preco_compras + juros
    valor_parcela = total_pagamento / numero_parcelas
    print(f'Sua compra será parcelada em {numero_parcelas}x de R${valor_parcela:.2f} com JUROS.')
    print(f'Sua compra de R${preco_compras:.2f} vai custar R${total_pagamento:.2f} no final.')
else:
    print('Opcão inválida. Tente novamente.')