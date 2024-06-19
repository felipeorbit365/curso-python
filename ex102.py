def fatorial(numero, show=False): # Parâmetro opcional, começa com False
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta;
    :return: O valor do Fatorial de um valor numero.
    """
    fatorial = 1
    for contador in range (numero, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fatorial = fatorial * contador
    return fatorial


print(fatorial(5, show=True)) # Muda manualmente para False ou True
help(fatorial)
