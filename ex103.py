def ficha(nome='<desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome_jogador = str(input('Nome do Jogador: '))
numero_gols = str(input('Número de Gols: '))

if numero_gols.isnumeric(): # Se for um número
    numero_gols = int(numero_gols) # Transforma a string em inteiro
else: # Se não for número, passa 0
    numero_gols = 0

if nome_jogador.strip() == '': # Se o nome do jogador estiver vazio
    ficha(gols=numero_gols) # Passa só os gols
else: # Se estiver com o nome preenchido
    ficha(nome_jogador, numero_gols) # Passa o nome e os gols


'''
Minha solução:

def ficha(nome=0, gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome_jogador = str(input('Nome do Jogador: '))
numero_gols = str(input('Número de Gols: '))
ficha(nome_jogador, numero_gols)

Meu jeito faria com que aparecesse 'três', por exemplo, se o usuário escrevesse.
No jeito do Guanabara, ele gostaria que nesse caso, mostrasse 0.
O restante está correto para aparição no terminal.

'''