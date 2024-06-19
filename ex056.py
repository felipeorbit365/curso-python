media = 0
soma_idade = 0
homem_velho = 0
mulheres_jovens = 0
nome_velho = ''

for contador in range(1,5):
    print(f'----- {contador}ª PESSOA -----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma_idade = soma_idade + idade 

    if sexo == 'M' and idade > homem_velho:
            homem_velho = idade
            nome_velho = nome
    if sexo == 'F' and idade < 20:
            mulheres_jovens = mulheres_jovens + 1

media = soma_idade / 4

print(f'Média de idade do grupo: {media:.1f} anos.')
print(f'O homem mais velho tem {homem_velho} anos e seu nome é {nome_velho}.')
print(f'Ao todo, {mulheres_jovens} mulheres têm menos de 20 anos.')

'''
Solução do Guanabara para atribuir a idade do homem mais velho ao seu nome:

if contador == 1 and sexo == 'M':
    homem_velho = idade 
    nome_velho = nome 
if sexo == 'M' and idade > homem_velho:
    homem_velho = idade
    nome_velho = nome

Não muda nada, o contador verifica a primeira pessoa e faz a atribuição.
Minha condição  if sexo == 'M' and idade > homem_velho: também faz a mesma coisa de forma resumida.
'''