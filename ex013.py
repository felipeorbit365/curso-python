salario = float(input('Informe o salário do funcionário: R$'))
aumento = salario + (salario * 15/100)
print('O salário de R${:.2f}, com 15% de aumento, passa a ser R${:.2f}'.format(salario, aumento))
