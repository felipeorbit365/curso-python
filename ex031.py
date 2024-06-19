distancia_viagem = float(input('Insira a distância da viagem: '))
print('Você começará uma viagem de {:.1f}Km.'.format(distancia_viagem))

if distancia_viagem <= 200:
    valor_passagem = distancia_viagem * 0.50
    print('Com o valor de R$0,50 por Km, sua passagem custa R${:.2f}'.format(valor_passagem))
else:
    valor_passagem = distancia_viagem * 0.45
    print('Com o valor de R$0,45 por Km, sua passagem de viagem mais longa custa R${:.2f}'.format(valor_passagem))

"""
O Guanabara faz apenas um print() para mostrar o valor da passagem, deixando sem identação
Ou seja, fora dos blocos verdadeiro/falso, o que faz com que o print() seja executado independentemente da condicional
Meu método está certo também.

Também é possível fazer com Se simplificado:
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45

O preço será multiplicado por 0.50 se a distância for abaixo de 200
Senão, será multiplicado por 0.45 se for maior que 200.
É a mesma coisa, mas é uma forma simplificada de fazer em uma única linha.
"""
