import math
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
print('A hipotenusa mede {:.2f}'.format(math.sqrt(hipotenusa)))


''' O quadrado da hipotenusa é igual a soma dos quadrados dos catetos
Para isso, é feita a raiz quadrada da hipotenusa 
Método sem importação, apenas a matemática: 
print('A hipotenusa mede {:.2f}'.format(hipotenusa ** (1/2)))
Também existe a funcionalidade específica para hipotenusa:
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
'''
