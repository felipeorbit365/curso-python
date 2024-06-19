total_numeros = 0
soma_numeros = 0

numero = int(input('Digite um número [999 para parar]: '))
while numero != 999:
    total_numeros = total_numeros + 1
    soma_numeros = soma_numeros + numero
    numero = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {total_numeros} números e a soma entre eles foi {soma_numeros}')
 
''' 
Colocando o input de numero fora do while também, o flag  é desconsiderado. Ele sai direto, não soma.
Depois é necessário ler o flag dentro também
Entretanto, essa não é a melhor solução. Repetir assim não é bom
Break resolve
'''