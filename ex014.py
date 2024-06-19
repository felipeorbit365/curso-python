temperatura_c = float(input('Informe a temperatura em ºC: '))
temperatura_f = temperatura_c * 1.8 + 32
print('A temperatura de {}ºC corresponde a {}ºF'.format(temperatura_c, temperatura_f))

# Também funciona, só mudando a fórmula: temperatura_f = ((9 * temperatura_c) / 5) + 32
# Os parênteses, nesse caso, não são realmente necessários, mas facilitam a leitura da expressão

