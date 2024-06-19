velocidade_carro = float(input('Velocidade atual do carro: '))
multa = (velocidade_carro - 80) * 7

if velocidade_carro <= 80:
    print('Na sua velocidade de {}Km/h, você está dentro do limite de 80 Km/h'.format(velocidade_carro))
else:
    print('MULTA! Você excedeu o limite permitido de 80 Km/h')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))

# Poderia ser só uma condição simples, utilizando o if para indicar se está acima de 80 Km/h
# De tal modo, dispensando o else, é só deixar o outro print()
# que fala sobre poder seguir em frente normalmente, sem a identação
# pois assim, será executado e está fora dos blocos verdadeiro/falso
