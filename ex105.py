# Minha solução
def notas(* notas_alunos, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas_alunos: uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicado se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """

    turma = {}
    
    turma['total'] = len(notas_alunos)
    
    # Inicializa maior_nota e menor_nota com a primeira nota para comparação
    if notas_alunos:  # Verifica se há pelo menos uma nota
        maior_nota = menor_nota = notas_alunos[0]
    else:
        maior_nota = menor_nota = 0  # Caso não haja notas, define ambas como 0
    for nota in notas_alunos:
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota
    turma['maior'] = maior_nota
    turma['menor'] = menor_nota

    soma_notas = 0
    for nota in notas_alunos:
        soma_notas = soma_notas + nota
    turma['media'] = soma_notas / len(notas_alunos)

    if situacao:
        if turma['media'] >= 7:
            turma['situacao'] = 'BOA'
        elif turma['media'] >= 5:
            turma['situacao'] = 'RAZOÁVEL'
        else:
            turma['situacao'] = 'RUIM'

    return turma  # Retorna o dicionário com as informações


resposta = notas(5.5, 2.5, 1.5, situacao=True)
print(resposta)

'''
Para o maior e menor valor, poderia ser apenas:

maior_nota = menor_nota = notas_alunos[0]

for nota in notas_alunos:
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
         menor_nota = nota
turma['maior'] = maior_nota
turma['menor'] = menor_nota
'''