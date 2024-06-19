maior_peso = 0
menor_peso = 0

for contador in range(1,6):
    peso_pessoas = float(input(f'Peso da {contador}ª pessoa: '))
    if contador == 1:
        maior_peso = peso_pessoas
        menor_peso = peso_pessoas
    else: 
        if peso_pessoas > maior_peso:
            maior_peso = peso_pessoas
        if peso_pessoas < menor_peso:
            menor_peso = peso_pessoas

print(f'O maior peso é {maior_peso}Kg')
print(f'O menor peso é {menor_peso}Kg')
 