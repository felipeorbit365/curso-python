from time import sleep

def contador(inicio, fim, passo):
    # Faz o teste lógico do passo para que não dê problemas com passos negativos
    if passo < 0: # Na personalização, dá erro se o número for negativo, então precisa analisar
        passo = passo * -1 # Joga o passo para positivo, trocando seu sinal
    if passo == 0: # Na personalização, caso o passo seja 0, faz virar 1, pois passo 0 não existe
        passo = 1

    print('-' * 40)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1) # Intervalo antes de contar

    if inicio < fim: # Ordem crescente
        contador_numeros = inicio
        while contador_numeros <= fim:
            print(f'{contador_numeros} ', end='', flush=True) # Flush faz o intervalo acontecer
            sleep(0.5) # Estiliza a contagem com espera de meio segundo
            contador_numeros = contador_numeros + passo # Adiciona o passo na ordem crescente
        print('FIM!')
    else: # Ordem decrescente, quando o início seria maior que o fim
        contador_numeros = inicio
        while contador_numeros >= fim:
            print(f'{contador_numeros} ', end='', flush=True) # Flush faz o intervalo acontecer
            sleep(0.5) # Estiliza a contagem com espera de meio segundo
            contador_numeros = contador_numeros - passo # Remove o passo na ordem decrescente
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-' * 40)
print('Agora é hora de personalizar a contagem!')
inicio_usuario = int(input('Início: '))
fim_usuario = int(input('Fim: '))
passo_usuario = int(input('Passo: '))
contador(inicio_usuario, fim_usuario, passo_usuario)

'''
Jeito que eu fiz, sem aparecer o 0 na contagem decrescente:

def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        for contador in range(inicio, fim+1, passo):
            print(f'{contador} ', end='')
        print('FIM!')
    else:
        for contador in range(inicio, fim, (-passo)):
            print(f'{contador} ', end='')
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

- Até então, funcional

---

Forma personalizada:

print('-' * 50)
print('Agora é hora de personalizar a contagem!')
inicio_usuario = int(input('Início: '))
fim_usuario = int(input('Fim: '))
passo_usuario = int(input('Passo: '))
contador(inicio_usuario, fim_usuario, passo_usuario)

- Está errado, pois bagunça os números caso sejam negativos

'''