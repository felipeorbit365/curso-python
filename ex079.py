lista_valores = []
continuar = ''
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista_valores:
        lista_valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 50)
lista_valores.sort()
print(f'Você adicionou os valores: {lista_valores}')
