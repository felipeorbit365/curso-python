from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # Abre arquivo em modo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # Escreve arquivo de texto e, caso não exista, cria
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        # Para cada linha dentro do arquivo, separa os ;
        # Dividindo os dados, através da lista, é escrito na tela
        # [0] é o nome e [1] é a idade
        # Para cadastrar pessoas, acontece um \n (na função de cadastro)
        # Para remover isso, substitui-se o \n por um vazio
        for linha in a: 
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at') # Coloca coisas no arquivo de texto
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


