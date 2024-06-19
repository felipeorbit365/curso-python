numero = 0 
contador = 0

while True:
    numero = int(input('Digite o número que deseja ver a tabuada: '))
    print('---------------------------------------------------')
    if numero < 0: # Faz a verificação logo depois de ler o número
        break
    for contador in range(1, 11):
        print(f'{numero} x {contador} = {numero * contador}')
    print('---------------------------------------------------')
print('PROGRAMA TABUADA ENCERRADO.')
