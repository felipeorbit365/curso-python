numero = 0
total_valores = 0
soma_valores = 0 

while True:
    numero = int(input('Digite um valor [999 para parar]: '))
    if numero == 999: # Antes de somar
        break # Interrompe o fluxo do laço antes de ver a soma e o total
    soma_valores = soma_valores + numero
    total_valores = total_valores + 1
print(f'A soma dos {total_valores} valores foi {soma_valores}.')
