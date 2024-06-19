from datetime import date 

ano_atual = date.today().year

pessoa = {}

pessoa['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = ano_atual - ano_nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho [0 se não tiver]: '))
if pessoa['ctps'] == 0:
    print('-' * 50)
    for k, v in pessoa.items():
        print(f'- {k} tem o valor {v}')
else:
    pessoa['ano de contratacao'] = int(input('Ano de Contratação: '))
    anos_exercidos = ano_atual - pessoa['ano de contratacao']
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + (35 - anos_exercidos)
    print('-' * 50)
    for k, v in pessoa.items():
        print(f'- {k} tem o valor {v}')

'''
 O  Guanabara fez assim para idade:

 Não há necessidade para ano_atual
 from datetime import datetime
 ano_nascimento = int(input('Ano de Nascimento: '))
 pessoa['idade'] = datetime.now().year - ano_nascimento

 Ele também inverteu a lógica do if:
 if pessoa['ctps'] != 0:
 Nisso, não precisa de else, já que só vai aumentar os dados no dicionário se for diferente de 0.
 Isso poupa linhas e o uso de laços de repetição para cada condicional.

 Para a lógica da aposentadoria, ele fez:
 pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratacao'] + 35) - datetime.now().year)
 Ele calcula o ano que irá se aposentar somando o ano de contratação com 35, menos o ano atual
 Com isso, soma a idade dele.
 '''