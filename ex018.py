import math
angulo = float(input('Digite o ângulo: '))

seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

'''
O (x) passado como parâmetro na função não está em graus centígrados, 
está em radianos. Por tal razão, o resultado não estará correto.
De tal modo, a conversão de radianos deve ser feita também. 
Pega o ângulo digitado, converte para radianos e calcula o seno do ângulo
convertido para radianos.
É possível aninhar uma chamada na outra.
'''