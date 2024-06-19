soma = 0 
contador = 0

for c in range(1,7):
    numero = int(input(f'Digite o {c}º valor: '))
    if numero % 2 == 0:
        soma += numero 
        contador += 1
print(f'Foram informados {contador} números pares, cuja soma é {soma}')
