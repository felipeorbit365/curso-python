valores = [] # Lista vazia
maior_valor = 0
menor_valor = 0
for contador in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {contador}: '))) 
    # Quando for o primeiro valor lido, ele é o menor e o maior também 
    if contador == 0: # Se for o primeiro valor lido
        maior_valor = menor_valor = valores[contador] # Inicializa o primeiro valor lido como o maior e o menor
    else: # Faz as verificações para analisar o valor lido de acordo com maior_valor e menor_valor
        if valores[contador] > maior_valor: # Verifica se o valor lido é maior que maior_valor. Se for, o maior_valor vira o valor lido
            maior_valor = valores[contador] # Atribui de acordo com o valor lido no momento
        if valores[contador] < menor_valor: # Verifica se o valor lido é menor que menor_valor
            menor_valor = valores[contador] # Atribui de acordo com o valor lido no momento
print('-' * 50)
print(f'Você digitou os valores: {valores}')   
print(f'O maior valor digitado foi {maior_valor} nas posições ', end='') # Indica a posição e continua na mesma linha
for indice, valor in enumerate(valores): # Para cada elemento da lista, verifica o maior para atribuição do índice
    if valor == maior_valor: # Se o elemento da lista for o maior
        print(f'{indice}...', end='') # Indica os índices, continuando na mesma linha (se houver mais de um)
print() # Quebra de linha
print(f'O menor valor digitado foi {menor_valor} nas posições ', end='') # Indica a posição e continua na mesma linha
for indice, valor in enumerate(valores): # Para cada elemento da lista, verifica o menor para atribuição do índice
    if valor == menor_valor: # Se o elemento da lista for o menor
        print(f'{indice}...', end='') # Indica os índices, continuando na mesma linha (se houver mais de um)
print() # Quebra de linha quando os índices (se houver mais de um) tiverem sido exibidos um ao lado do outro

"""
Solução dos comentários no YouTube:

valores = []
for cont in range (0,5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))  # ADICINANDO VALORES NA LISTA
print (f'Os valores digitados: {valores}')

print (f'O maior valor digitado foi: {max(valores)}, nas posições: ',end=' ')
for posicao, valor in enumerate(valores):   # P = POSIÇÃO (ÍNDICE), V = VALORES
    if  valor == max(valores):
        print (f'{posicao}...')

print(f'O menor valor digitado foi: {min(valores)}, nas posições: ', end=' ')
for posicao, valor in enumerate(valores):
    if valor == min(valores):
        print (f'{posicao}...' ,end='')

---------------------------------------------------

Comentário no YouTube para facilitar entendimento:

Uma coisa que pude perceber, mesmo que seja idiota e que muitos já tenham percebido antes(eu só percebi agora e
 notei que me ajudou com o entendimento para manusear, montar e aplicar as funções, for, enumerate e outras).

O sistema SEMPRE considera( lê ) primeiro os indices e depois os valores/conteúdos dos itens na lista e tupla.

* Exemplos:

for i, v in enumerate(lista)
Primeiro começa com o índice, depois o conteúdo. 
Identificado o indice com o ' i ' minúsculo e o conteúdo/valor pelo '  v  ' minúsculo.


* Exemplo dado da aula de tupla:

for pos, comida in enumerate(lista)
O pos é o indice, sempre ele primeiro, não importa qual identificação se dê a ele,  como pos(de posição), i(de indice no exemplo anterior).


* Exemplo dado da aula de tupla:

for cont in range( 0, len(lista) ):
          print( f ‘ Eu vou comer { lista [cont] } na posição { cont } ’ )

O indice aqui esta representado por um contador(cont) que vai ser usado para correr com o laço for e correr o indice da tupla.   
'   lista[ cont ]  '   é o conteúdo da lista com o indice que está sendo varrido naquela vez do laço.    
Veja que em    ' na posição { cont } '    vai mostrar o indice. Perceba que ele aparece como primeiro item na declaração do for.
"""