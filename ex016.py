import math
numero_real = float(input('Digite um número real:'))
parte_inteira = math.trunc(numero_real)
print('O número real {} tem a parte inteira {}'.format(numero_real, parte_inteira))

''' Ou simplesmente:
print('O número real {} tem a parte inteira {}'.format(numero_real, math.trunc(numero_real)))
A criação de uma variável à parte é desnecessária
Também poderia ter importado apenas a função truncate:
from math import trunc
Desse modo, math. deixa de ser utilizado no código
print('O número real {} tem a parte inteira {}'.format(numero_real, trunc(numero_real))) 
Sem a importação da biblioteca, daria para fazer apenas a conversão para inteiro
print('O número real {} tem a parte inteira {}'.format(numero_real, int(numero_real))) 
'''
