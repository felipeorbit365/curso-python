from datetime import date 

ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento
print(f'O(a) atleta tem {idade} anos.')

if idade <= 9: 
    print('Classificação: MIRIM')
elif idade <= 14: 
    print('Classificação: INFANTIL')
elif idade <= 19: 
    print('Classificação: JÚNIOR')
elif idade <= 25: 
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

''' Não precisa especificar idade > 9 and idade <= 14, por exemplo.
O teste é desnecessário pois já passou como uma não possibilidade  no anterior.
Isto é, ao verificar o menor ou igual a 9 anteriormente, ele já sabe que não é quando passa para a próxima condição.
Logo, só pode estar acima de 9 - nesse caso.'''