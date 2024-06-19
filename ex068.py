from random import randint

resultado = ' '
soma_numeros = 0
usuario_vitorias = 0

print('-=-' * 10)
print('JOGO - PAR OU ÍMPAR')
print('-=-' * 10)

while True:
    numero_usuario = int(input('Digite um valor: '))
    aposta_usuario = ' ' # Deixa a aposta indefinida até que faça parte dos requisitos
    while aposta_usuario not in 'PI': # Repete para escrever a aposta até que seja 'P' ou 'I', não aceita qualquer coisa. Ex.: 'abc'.
        aposta_usuario = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0] # Exclui espaços, passa para maiúsculas e pega o 1º caractere
    print('-' * 30)
    numero_computador = randint(1, 10)
    soma_numeros = numero_usuario + numero_computador
    if soma_numeros % 2 == 0:
        resultado = 'PAR'
    else: 
        resultado = 'IMPAR'
    print(f'Você jogou {numero_usuario} e o computador jogou {numero_computador}')
    print(f'O total é {soma_numeros} - Resultado: {resultado}')
    print('-' * 30)
    if aposta_usuario == resultado[0]: # Pega o 1º caractere de 'resultado' | 'PAR' - > 'P' e 'IMPAR' -> 'I'
        print('PARABÉNS! Você venceu.')
        print('Vamos jogar novamente...')
        print('-' * 30)
        usuario_vitorias = usuario_vitorias + 1
    else:
        print(f'GAME OVER! Você venceu {usuario_vitorias} vez(es).')
        break

'''
Resolução do Guanabara: 

from random import randint

usuario_vitorias = 0

print('-=-' * 10)
print('JOGO - PAR OU ÍMPAR')
print('-=-' * 10)

while True:
    numero_usuario = int(input('Digite um valor: '))
    numero_computador = randint(1, 10)
    soma_numeros = numero_usuario + numero_computador
    aposta_usuario = ' '
    while aposta_usuario not in 'PI':
        aposta_usuario = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print('-' * 30)
    print(f'Você jogou {numero_usuario} e o computador jogou {numero_computador}')
    print(f'O total é {soma_numeros}')
    print('Resultado - PAR' if soma_numeros % 2 == 0 else 'Resultado - ÍMPAR')
    if aposta_usuario == 'P':
        if soma_numeros % 2 == 0:
            print('PARABÉNS! Você venceu.')
            usuario_vitorias = usuario_vitorias + 1
        else:
            print('Você perdeu.')
            break
    elif aposta_usuario == 'I': 
        if soma_numeros % 2 == 1:
            print('PARABÉNS! Você venceu.')
            usuario_vitorias = usuario_vitorias + 1
        else:
            print('Você perdeu.')
            break
    print('Vamos jogar novamente...')
    print('-' * 30)
print('-' * 30)
print(f'GAME OVER! Você venceu {usuario_vitorias} vez(es).')

--- 

A diferença entre o meu e o do Guanabara é que no meu a variável resultado 
é utilizada para armazenar se a soma é par ou ímpar e depois compara o primeiro caractere. 
O código do Guanabara avalia diretamente a condição dentro das estruturas de controle de fluxo.

O meu também aparece IMPAR sem acento Í já que a verificação é feita com o 1º caractere ao pedir por 'P' ou 'I'.

Eu fiz a comparação do resultado a partir da condição do resultado de ser par ou ímpar.
'''