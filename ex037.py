numero = int(input('Digite um número inteiro: '))

print('''OPÇÕES PARA CONVERSÃO 
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

opcao = int(input('Escolha opção para conversão: '))

if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para OCTAL é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é {hex(numero)[2:]}')
else:
    print('Essa não é uma opção.')
