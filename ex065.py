resposta_usuario = 'S' # É atribuído 'S' para inicializar o while
total_numeros = 0
soma_numeros = 0
media = 0
maior_numero = 0
menor_numero = 0

while resposta_usuario == 'S':
    numero = int(input('Digite um número: '))
    soma_numeros = soma_numeros + numero
    total_numeros = total_numeros + 1

    if total_numeros == 1:
        maior_numero = numero
        menor_numero = numero
    else:
        if numero > maior_numero:
            maior_numero = numero
        if numero < menor_numero:
            menor_numero = numero

    resposta_usuario = str(input('Deseja continuar? [S/N] ')).upper()

media = soma_numeros / total_numeros

print(f'Você digitou {total_numeros} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior_numero} e o menor valor foi {menor_numero}')

'''
Como descobrir menor e maior valor: 

Atribui um contador de modo que a contagem comece em 1 
e vá aumentando de acordo com a quantidade de novos valores que serão inseridos.
Enquanto estiver em 1, atribua o valor inicial para as duas variáveis, 
tanto a maior, quanto a maior, terão o mesmo valor atribuído inicialmente. 
Assim, por exemplo -> if total_numeros == 1
Após isso, será possível fazer a análise de acordo com os outros valores inseridos,
já que o contador irá para o segundo e a condição 'if total_numeros == 1' não será mais verdadeira, 
indo para o 2 e, de tal modo, caindo na condição do else com as análises,
para descobrir o maior e o menor valor corretamente
'''