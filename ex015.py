dia_aluguel = int(input('Insira o número de dias pelos quais o carro foi alugado: '))
km_percorridos = float(input('Insira a quantidade de Km percorridos: '))
valor_pagamento = (dia_aluguel * 60) + (km_percorridos * 0.15)
print('Total a pagar: R${:.2f}'.format(valor_pagamento))
