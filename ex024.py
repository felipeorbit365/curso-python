cidade = str(input('Insira a cidade que você nasceu: ')).strip()
print(cidade[:5].upper() == 'SANTO')

"""
O método do Guanabara procura entre a letra 0 e 4, as 5 primeiras letra
O dele funciona com o traço, mas aceita erros como Santos e Santorini

Minha solução, diferente da correção do Guanabara, mas funcional:
cidade = str(input('Insira a cidade que você nasceu: ')).strip().capitalize()
print('Santo' in cidade)

Comentário interessante no YouTube:
Caso o primeiro nome tenha que ser "Santo", acho melhor dessa forma abaixo, pois na do exemplo uma cidade como "Santorini" iria dar True:

c = input('Digite o nome da cidade: ').strip().replace('-', ' ').split()
print(c[0].upper() == 'SANTO')

Dessa forma só dá True se o nome for realmente "Santo". O replace serve para retornar True em cidades com hífen,
tal como Santo-Inácio. Sem fazer a substituição, retornaria False.

O operador == é mais recomendado que o in nesse caso.
"""
