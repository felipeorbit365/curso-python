valor_casa = float(input('Valor da casa: R$'))
salario_comprador = float(input('Salário do comprador: R$'))
anos_financiamento = int(input('Anos de financiamento: ')) 
parcelas = anos_financiamento * 12
prestacao = valor_casa / parcelas

print(f'Para pagar uma casa no valor de R${valor_casa:.2f} em {anos_financiamento} anos, a prestação mensal será de R${prestacao:.2f}')
if prestacao <= salario_comprador * 30/100:
    print('Empréstimo CONDEDIDO!')
else: 
    print('Empréstimo NEGADO!')
