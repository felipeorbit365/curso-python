import random
aluno_um = str(input('Primeiro aluno: '))
aluno_dois = str(input('Segundo aluno: '))
aluno_tres = str(input('Terceiro aluno: '))
aluno_quatro = str(input('Quarto aluno: '))
turma = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
aluno_escolhido = random.choice(turma)
print('O aluno escolhido foi {}'.format(aluno_escolhido))
