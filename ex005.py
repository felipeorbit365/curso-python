numero = int(input('Digite seu número: '))
antecessor = numero - 1
sucessor = numero + 1
print('Analisando o valor {}, seu antecessor é {} e seu sucessor é {}'.format(numero, antecessor, sucessor))
# É possível também fazer o cálculo na máscara de caracteres, com o .format() realizando a operação
# Exemplo: .format(numero, (numero - 1), (numero + 1)
# Dessa forma, apenas uma variável é utilizada. Seria interessante fazer outras caso fossem manipuladas
# individualmente no código. Quanto menos variáveis, menos memória será utilizada no dispositivo.
