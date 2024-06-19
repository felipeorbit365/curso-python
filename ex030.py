numero = int(input('Insira um número: '))

if (numero % 2) == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é ÍMPAR'.format(numero))

# Se o resto da divisão do número por 2 for igual a zero, ou seja, sem resto, é par.
# Se há resto, é ímpar.
# Eu realizei direto, mas está certo. Não criei uma nova varíavel.
"""
Exemplo:
numero = int(input('Insira um número: '))
resultado = numero % 2
print('O resultado é {}'.format(resultado)
O resto da divisão de qualquer número por 2: 
Se for 1, é ímpar. Se for 0, é par. 
Essa é a lógica do operador para o resto da divisão.
"""