from time import sleep

def maior(* numeros):
    print('-' * 40)
    print('Analisando os valores passados...')
    total_numeros = 0
    maior_numero = 0
    for numero in numeros: 
        print(f'{numero} ', end='', flush=True)
        sleep(0.3)
        total_numeros = total_numeros + 1
        if numero > maior_numero:
            maior_numero = numero
    print(f'\nForam informados {total_numeros} valores ao todo.')
    print(f'O maior valor informado foi {maior_numero}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6) 
maior()

'''
Para analisar o maior valor, o Guanabara fez:

cont = maior = 0

for valor in núm:
    if cont == 0:
        maior = valor
    else:
        if valor > maior:
            maior = valor
    contador += 1

--- Essa forma é preferível, pois indica que o maior valor é o primeiro valor informado
Da forma como eu fiz, atribuindo 0, seria um problema para números negativos.
Nesse exercício não tem, então está correto, mas é importante se atentar.

Exemplo:

Se houvesse: maior(-10, -20, -30)
Indicaria que o maior valor é 0, pois eu inicializei o maior_numero como 0 no código 
Isso não faria a análise apropriada de números negativos, já que nunca teria um número maior que 0 para atribuir

Da forma como o Guanabara fez, -10 seria o maior número dentre os valores fornecidos -10, -20, e -30
Isso porque o algoritmo estabelece o primeiro número como o maior na primeira iteração (quando cont == 0) 
Em seguida, compara esse valor com os subsequentes para determinar o maior de todos eles
Como -10 é maior que -20 e -30, ele é corretamente identificado como o maior valor
'''
