primeiro_valor = int(input('Primeiro valor: '))
segundo_valor = int(input('Segundo valor: '))
opcao = 0

while opcao != 5: 
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        print(f'A soma entre {primeiro_valor} e {segundo_valor} é {primeiro_valor + segundo_valor}')
    elif opcao == 2:
        print(f'A multiplicação entre {primeiro_valor} e {segundo_valor} é {primeiro_valor * segundo_valor}')
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print(f'O maior valor é {primeiro_valor}')
        else:
            print(f'O maior valor é {segundo_valor}')
    elif opcao == 4:
        primeiro_valor = int(input('Primeiro valor: '))
        segundo_valor = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
print('Fim do programa!')
