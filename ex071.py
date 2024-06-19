print('-------')
print(' BANCO ')
print('-------')
valor_saque = int(input('Valor a ser sacado: R$'))
total_montante = valor_saque # O montante é o valor do saque
cedula = 50 # Cédula de maior valor no sistema
total_cedulas = 0

"""
Do montante, se tira 50 reais quantas vezes forem necessárias para analisar a necessidade de cédulas de 50 reais
Após isso, o mesmo é verificado com o restante das cédulas. 
"""

while True: # Loop é quebrado quando o valor total for correspondido
    if total_montante >= cedula: # Tenta tirar 50 do valor. Se dá pra tirar 50, tira 50 quantas vezes for necessário
        total_montante = total_montante - cedula
        total_cedulas = total_cedulas + 1 # O total de cédulas que representa quantas vezes 50 foi tirado do total
    else:
        if total_cedulas > 0: # Faz com que não escreva se o total de cédulas for 0, ou seja, só mostra as cédulas utilizadas
            print(f'Total de {total_cedulas} cédulas de R${cedula}')
        if cedula == 50: # Se a cédula atual for 50 e não for possível tirar  - mais ou nada - 50, passa a tirar 20
            cedula = 20
        elif cedula == 20: 
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0 # Cada vez que muda a nota, o total de cédulas utilizadas volta para 0. Cada cédula tem seu total
        if total_montante == 0: # A análise é feita de cédula para cédula até acabar o valor do montante
            break # Total correspondido, encerrando o sistema
print('-------')
print('Saque feito!')

# Este código simula o funcionamento de um caixa eletrônico. O usuário informa o valor desejado para saque,
# e o programa calcula a quantidade de cédulas de R$50, R$20, R$10 e R$1 necessárias para atender ao valor solicitado.
# O loop principal percorre as cédulas em ordem decrescente de valor, subtraindo o valor da cédula do total a ser sacado
# e contabilizando a quantidade de cédulas utilizadas. O programa imprime o resultado para cada tipo de cédula
# e finaliza quando todo o valor foi contabilizado.

"""
Ou seja, sobre a parte principal da lógica:

Se o valor da cédula (cedula) é menor ou igual ao valor restante (total_montante), 
subtrai esse valor do total e incrementa o número de cédulas.
Caso contrário, se o valor da cédula é maior que o restante, a lógica dentro do else é acionada.

Se houver cédulas retiradas, imprime o total de cédulas da denominação atual.
Atualiza a cédula para a próxima denominação (de R$50 para R$20, R$20 para R$10, etc.).
Reinicia o contador de cédulas (total_cedulas).
"""