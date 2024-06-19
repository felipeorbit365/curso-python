lista_pessoas = list()
dados = list()
maior_peso = 0
menor_peso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista_pessoas) == 0: # O len() da lista é 0 porque inicializa no índice 0
        maior_peso = menor_peso = dados[1] # Inicializa o peso com dados[1]
    else: # Conforme mais gente é cadastrada, o len() aumenta e analisa o peso de acordo
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    lista_pessoas.append(dados[:])
    dados.clear()

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 50)
print(f'Ao todo, você cadastrou {len(lista_pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de ', end='')
for pessoa in lista_pessoas: # Percorre cada item da lista 
    if pessoa[1] == maior_peso: # pessoa[1] é o peso de cada pessoa, daí atribui se for o maior_peso
        print(f'[{pessoa[0]}] ', end='') # pessoa[0] são os nomes, atribuindo de acordo
print() # Isso foi feito para pular para a linha abaixo, já que o end='' acima está sendo utilizado para mostrar todos os nomes de quem tem o maior_peso
print(f'O menor peso foi de {menor_peso}Kg. Peso de ', end='')
for pessoa in lista_pessoas:
    if pessoa[1] == menor_peso:
        print(f'[{pessoa[0]}] ', end='')
print()

'''
Forma como eu tinha feito para o maior e menor peso:

    for contador in range(0, len(lista_pessoas)): 
        if contador == 0:
            maior_peso = lista_pessoas[contador][1]
            menor_peso = lista_pessoas[contador][1]
        else:
            if lista_pessoas[contador][1] > maior_peso:
                maior_peso = lista_pessoas[contador][1]
            if lista_pessoas[contador][1] < menor_peso:
                menor_peso = lista_pessoas[contador][1]
---
Comentário no YouTube:

Jeito do Guanabara 
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')


Forma alternativa
for nome, peso in princ:
    if peso == men:
        print(nome, end=' ')
---
Sugestão do Bard/Gemini:

nomes_maior_peso = []
nomes_menor_peso = []
for pessoa in lista_pessoas:
    if pessoa[1] == maior_peso:
        nomes_maior_peso.append(pessoa[0])
    if pessoa[1] == menor_peso:
        nomes_menor_peso.append(pessoa[0])

print(f'Ao todo, você cadastrou {len(lista_pessoas)} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de {" e ".join(nomes_maior_peso)}.')
print(f'O menor peso foi de {menor_peso}Kg. Peso de {" e ".join(nomes_menor_peso)}.')
'''
