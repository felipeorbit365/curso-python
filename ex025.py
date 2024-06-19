nome = str(input('Digite seu nome completo: ')).title().strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome))

# Nesse exercício, nome[:5] não adiantaria pois só verificaria as 5 primeiras letras
# Silva pode aparecer em qualquer lugar.
# CORREÇÃO GUANABARA:
# nome = str(input('Digite seu nome completo: ')).title().strip()
# print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper))
# in não é metodo, é um operador Python

"""
Comentário interessante no YouTube
O "problema" é que assim alguém com o nome de Silvana iria entrar como positivo também. Colocando isso como restrição, fiz o meu assim:

nome = str(input('Qual o seu nome? ')).strip()
print('Seu nome possui "SILVA"? {}'.format('SILVA' in nome.upper().split()))
"""