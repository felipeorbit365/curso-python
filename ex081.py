lista_valores = []

while True:
    valor = int(input('Digite um valor: '))
    lista_valores.append(valor)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 50)
print(f'Você digitou {len(lista_valores)} elementos.')
lista_valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista_valores}')
if 5 in lista_valores:
    print('O valor 5 faz parte da lista')
else: 
    print('O valor 5 não foi encontrado na lista!')
