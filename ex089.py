ficha_aluno = []

while True:  
    nome = str(input('Nome: '))
    nota_um = float(input('Nota 1: '))
    nota_dois = float(input('Nota 2: '))
    media = (nota_um + nota_dois) / 2
    ficha_aluno.append([nome, [nota_um, nota_dois], media]) # Adiciona os dados na lista composta    

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}') # Formata o estilo alinhando à esquerda e direita da forma como aparece no terminal apenas
print('-' * 30)

for indice, aluno in enumerate(ficha_aluno): # Mostra os dados dos alunos percorrendo a lista
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>8.1f}') # Exibe de acordo com a formatação de estilo. Na lista, [0] é o Nome e [2] são as notas

while True:
    print('-' * 30)
    escolha_aluno = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if escolha_aluno == 999:
        print('FINALIZANDO...')
        break
    if escolha_aluno <= len(ficha_aluno) - 1: # Tem que ser menor que a quantidade de alunos cadastrados econsiderando que o primeiro é 0
        print(f'Notas de {ficha_aluno[escolha_aluno][0]} são {ficha_aluno[escolha_aluno][1]}') # Se for menor, mostra as notas do aluno. 
        # [escolha_aluno] é o número (índice) do aluno
        # [0] é o nome do aluno 
        # [1] são as notas do aluno
