# Cada pessoa é um dicionário 
# Todos os dicionários são uma lista 
pessoa = {}
lista_pessoas = []
soma_idades = 0
media = 0
lista_mulheres = []
lista_acimaMedia = []

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Opção inválida. Sexo: [M/F] ')).strip().upper()[0]
    if pessoa['sexo'] == 'F':
        lista_mulheres.append(pessoa['nome']) # Armazena apenas o nome da mulher na lista de mulheres
    pessoa['idade'] = int(input('Idade: '))
    lista_pessoas.append(pessoa.copy())
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN': 
        continuar = str(input('Opção inválida. Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

for pessoa in lista_pessoas: # Percorre cada item na lista_pessoas
    soma_idades = soma_idades + pessoa['idade'] # Obtém a soma das idades acessando as idades de cada pessoa da lista
media = soma_idades / len(lista_pessoas) # A soma das idades é dividida pelo total de pessoas, obtido pelo len()

for pessoa in lista_pessoas: # Percorre cada item da lista_pessoas
    if pessoa['idade'] > media: # Se a idade de cada pessoa percorrida na lista for maior que a média
        lista_acimaMedia.append(pessoa) # Adiciona todos os dados da pessoa percorrida da vez na lista de acima da média

print('-' * 60)
print(f'A) Ao todo temos {len(lista_pessoas)} cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: {lista_mulheres}')
print(f'D) Lista de pessoas que estão com a idade acima da média: {lista_acimaMedia}')
# Poderia fazer:
# print('D) Lista de pessoas que estão com a idade acima da média:')
# for pessoa in lista_acimaMedia:
   # print(f"Nome: {pessoa['nome']}, Sexo: {pessoa['sexo']}, Idade: {pessoa['idade']}\n")
print('--- ENCERRADO ---')

'''
O Guanabara não queria uma lista de mulheres, nem uma lista para acima da média.
Entretanto, esse código atende os requisitos, só não está no seu "estilo".
Confira ex094b.py para ver como o Guanabara fez.
'''