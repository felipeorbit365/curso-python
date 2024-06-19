nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
palavras = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(palavras[0], len(palavras[0])))

""" 
É possível usar o .strip() diretamente, mas os espaços entre
as palavras são mantidos, portanto tem que ser o tamanho
do nome menos o espaços. A função .count() com ' ' conta
os espaço, para aí depois poder retirá-los do len() com a subtração. 
Conta a quantidade de espaços. Sendo assim: a quantidade de letras com espaço menos 
quantos espaços têm, eliminando-os.
Para encontrar o primeiro nome, utilizar .find(' ')
para encontrar o primeiro espaço. Encontrando ele, é possível
definir quantas letras tem o primeiro nome.

Exemplo:
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

Separar os nomes também é uma alternativa.
Crie uma lista com .split(), separando cada uma das palavras.
O [0] indica que é a primeira palavra, pois a contagem começa no zero.

"""