# Solução do Guanabara, sem listas para mulheres e pessoas com idade acima da média
pessoa = {}
lista_pessoas = []
soma_idades = 0
media = 0

while True:
    pessoa.clear() # Antes de ler o nome, esvazia a cada pessoa nova no laço antes de colocar na lista
    pessoa['nome'] = str(input('Nome: '))
    while True: 
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma_idades = soma_idades + pessoa['idade']
    lista_pessoas.append(pessoa.copy())
    while True: 
        resposta_usuario = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta_usuario in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta_usuario == 'N':
        break
print('-' * 60)
print(f'A) Ao todo temos {len(lista_pessoas)} cadastradas.')
media = soma_idades / len(lista_pessoas)
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for pessoa in lista_pessoas:
    if pessoa['sexo'] in 'Ff':
        print(f'{pessoa["nome"]} ', end='')
print()
print(f'D) Lista de pessoas que estão com a idade acima da média: ')
for pessoa in lista_pessoas:
    if pessoa['idade'] >= media:
        print('     ', end='') # Estiliza as linhas só
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('--- ENCERRADO ---')
