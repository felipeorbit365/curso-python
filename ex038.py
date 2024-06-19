primeiro_numero = int(input('Digite o primeiro número: '))
segundo_numero = int(input('Digite o segundo número: '))

if primeiro_numero > segundo_numero:
    print('O primeiro valor é maior.')
elif segundo_numero > primeiro_numero:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
    