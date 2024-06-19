# Forma correta do Guanabara: from ex115.lib.interface import * 
# O sistema não reconhece o módulo, não entendi o motivo, mas do jeito abaixo funciona
from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema
        cabecalho('Saindo do sistema... Até logo!')
        break
    else: 
        print('ERRO! Digite uma opção válida!')
    sleep(2)


"""
Lógica para criar arquivos:

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else: 
    print('Arquivo não encontrado!')
    criarArquivo(arq)
"""
