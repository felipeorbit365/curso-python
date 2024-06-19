expressao = str(input('Digite a expressão: '))
pilha = []

for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Expressão válida! Todos os parênteses estão corretos.')
else:
    print('Expressão inválida! A ordem dos parênteses está incorreta.')

"""
É utilizada uma pilha para rastrear os parênteses abertos. 
Percorremos cada caractere da expressão, e se encontrarmos um parêntese de abertura, adicionamos à pilha. 
Se encontrarmos um parêntese de fechamento, verificamos se a pilha não está vazia antes de remover um parêntese de abertura.
Se a pilha estiver vazia no final, todos os parênteses foram fechados corretamente. Caso contrário, a expressão é considerada inválida.

Explicação do Guanabara:
Cada vez que abre parênteses, adiciona-se um parênteses na pilha. 
Quando acha um parênteses fechando, é removido o parênteses que foi aberto.
Isto é, cada vez que abre, coloca-se um parênteses abrindo. Cada vez que fecha, remove o parênteses que foi aberto.
Foi encontrado "o par" do parênteses. Foi satisfeito.
Caso a pilha esteja vazia, é colocado um parênteses fechando e dá break, significando que a pilha não está vazia. Dando erro.
"""
