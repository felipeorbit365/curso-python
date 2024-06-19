salario = float(input('Valor do salário: R$'))

if salario > 1250:
    aumento = salario + (salario / 100 * 10)
    print('O salário no valor de R${:.2f} tem aumento de 10% e passa a ser R${:.2f}'.format(salario, aumento))
else:
    aumento = salario + (salario / 100 * 15)
    print('O salário no valor de R${:.2f} tem aumento de 15% e passa a ser R${:.2f}'.format(salario, aumento))

"""
Forma alternativa:
if salario <= 1250:
    aumento = salario + (salario * 15 /100)

else:
    aumento = salario + (salario * 10 /100)
print('O salário no valor de R${:.2f} tem aumento e passa a ser R${:.2f}'.format(salario, aumento))

O print também poderia ficar fora do if/else, pois é executado se estiver fora dos blocos.
Entretanto, não será tão personalizado mostrando a porcentagem de aumento correspondente. 
Para o cálculo de aumento: é o salário, mais o valor da porcentagem de aumento do salário.
"""
