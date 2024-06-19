frase = str(input('Digite uma frase: ')).strip().upper()
palavras_separadas = frase.split()
palavras_juntas = ''.join(palavras_separadas)
frase_inversa = ''

for letra in range(len(palavras_juntas) - 1, -1, -1):
    frase_inversa += palavras_juntas[letra]
print(f'O inverso de {palavras_juntas} é {frase_inversa}')

if frase_inversa == palavras_juntas:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')

'''
Macete de fatiamento:

frase_inversa = palavras_juntas[::-1]

Desse modo, deixa inverso também, mas sem fazer o laço de repetição.
'''