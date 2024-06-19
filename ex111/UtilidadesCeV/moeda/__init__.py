def aumentar(preco=0, taxa=0, formatado=False):
    resultado = preco + (preco * taxa/100)
    return resultado if formatado is False else moeda(resultado)


def diminuir(preco=0, taxa=0, formatado=False):
    resultado = preco - (preco * taxa/100)
    return resultado if formatado is False else moeda(resultado)


def dobro(preco=0, formatado=False):
    resultado = preco * 2
    return resultado if formatado is False else moeda(resultado)


def metade(preco=0, formatado=False):
    resultado = preco / 2
    return resultado if formatado is False else moeda(resultado)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',') 


def resumo(preco=0, taxa_aumento=10, taxa_reducao=5):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxa_aumento}% de aumento: \t{aumentar(preco, taxa_aumento, True)}')
    print(f'{taxa_reducao}% de redução: \t{diminuir(preco, taxa_reducao, True)}')
    print('-' * 35)

