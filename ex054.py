from datetime import date 
ano_atual = date.today().year

maiores_idade = 0
menores_idade = 0 

for contador in range(1,8):
    ano_nascimento = int(input(f'Ano de nascimento da {contador}ª pessoa: '))
    idade_pessoa = ano_atual - ano_nascimento
    if idade_pessoa >= 18:
        maiores_idade = maiores_idade + 1
    else: 
        menores_idade = menores_idade + 1

print(f'{maiores_idade} dessas pessoas são maiores de idade')
print(f'{menores_idade} dessas pessoas são menores de idade')
