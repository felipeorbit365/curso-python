nome = str(input('Digite seu nome completo: ')).split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))

# O len é capaz de verificar quantas posições tem. De tal modo, é utilizado, verifica e subtrai 1 para
# indicar a última posição, já que sempre deve ser indicado 1 a mais, 
# pois o próprio programa já não conta o último.
# Sempre conta um a menos porque a contagem começa do 0.
# -1 dentro dos colchetes pois indica a posição.
