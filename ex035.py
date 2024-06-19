print('-=-' * 8)
print('Analisador de Triângulos')
print('-=-' * 8)
primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))

# Para três segmentos fecharem um triângulo, cada lado deve ser menor que a soma dos outros dois.
# Cada um dos segmentos, tem que ser menor do que a soma do comprimento dos outros dois.
if primeiro < (segundo + terceiro) and segundo < (primeiro + terceiro) and terceiro < (primeiro + segundo):
    print('Os segmentos acima PODEM formar um triângulo.')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')

"""
Nesse caso, o print() muda de acordo com a condicional, por isso não é possível fazer fora dos blocos.
Os segmentos também poderiam ficar fora dos parênteses.
"""