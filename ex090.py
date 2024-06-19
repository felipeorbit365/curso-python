aluno = {}

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7: # Média entre 5 e 7, não é '<=7'  já que se for 7 é aprovado 
    aluno['situacao'] = 'Recuperação'
else: 
    aluno['situacao'] = 'Reprovado'
print('-' * 30)
# Percorre os elementos do dicionário
# .items() -> Conjunto chave e valor
for k, v in aluno.items(): # Para cada chave (k/key), um valor (v/value) no dicionário aluno
    print(f'{k} é igual a {v}')
# K/Key -> nome, media, situacao
# V/Value -> As duas primeiras respostas do usuário e o resultado da análise da situação

'''
Eu fiz escrevendo as chaves diretamente porque não entendi inicialmente 
que era a chave em si demonstrada que o professor queria 
(KKKKK em minha defesa ele não deixou tão claro, mas depois que percebi como deveria ser feito, fiz de primeira)

print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situacao"]}')
'''
  