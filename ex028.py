import random
from time import sleep

numero_computador = random.randint(0, 5)

print('-=-' * 12)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-' * 12)
numero_usuario = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if numero_computador == numero_usuario:
    print('VOCÊ VENCEU! Parabéns, eu realmente pensei no número {}'.format(numero_computador))
else:
    print('O COMPUTADOR VENCEU! Eu pensei no número {}, não no número {}'.format(numero_computador, numero_usuario))
