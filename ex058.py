import random
numero_computador = random.randint(0, 10)

numero_tentativas = 0 

print('Sou seu computador...')
print('Acabei de pensar em número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

palpite = int(input('Digite seu palpite: ')) 

while palpite != numero_computador:
    if palpite < numero_computador:
        print('Pensei em número maior... Tente outra vez!')
        palpite = int(input('Digite seu palpite: '))
        numero_tentativas = numero_tentativas + 1
    else: 
        print('Pensei em número menor... Tente outra vez!')
        palpite = int(input('Digite seu palpite: '))
        numero_tentativas = numero_tentativas + 1
numero_tentativas = numero_tentativas + 1
print(f'Pensei no número {numero_computador}')
print(f'Você acertou com {numero_tentativas} tentativas. Parabéns!')


"""
Guanabara criou uma variável boleana "acertou" que inicia False

O código não é esse, mas o sentido da lógica foi:
acertou = False
while not acertou
if jogador == computador 
acertou == True
"""