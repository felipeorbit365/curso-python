def escreva(texto):
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))


escreva('Olá, Mundo!')

'''
Guanabara fez uma forma que adiciona espaços antes e depois: 

def escreva(texto):
    tamanho = len(texto) + 4 # São 2 para um lado e 2 para o outro, por isso 4
    print('-' * tamanho)
    print(f'  {texto}') # Dois espaços iniciais
    print('-' * tamanho)


escreva('Olá, Mundo!')

O meu acompanha o tamanho exato de caracteres.
'''