extenso = ('zero', 'um', 'dois', 'três', 'quatro', 
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'catorze',
          'quinze', 'dezesseis', 'dezessete', 
          'dezoito', 'dezenove', 'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0 <= numero <= 20: # if numero >= 0 and numero <= 20:
        break # Quando o usuário insere um número válido (entre 0 e 20), sai do laço e mostra o número por extenso
    print('Tente novamente. ', end='')
print(f'Você digitou o número {extenso[numero]}')


'''
Solução de comentário no YouTube:

numero = int(input('Digite um número ente 0 e 20: '))
while numero not in range(0,21):
	numero = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'Você digitou o numero {extenso[numero]}')
'''
