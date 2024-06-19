# Solução do Guanabara
def notas(* notas_alunos, situacao=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notas_alunos: uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicado se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """

    turma = {}
    
    turma['total'] = len(notas_alunos)
    turma['maior'] = max(notas_alunos)
    turma['menor'] = min(notas_alunos)
    turma['media'] = sum(notas_alunos)/len(notas_alunos)

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
help(notas)
