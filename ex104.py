def leiaInt(numero_usuario):
    validacao = False # Começa com False, pois ainda não foi validado
    valor = 0 # Inicializado para poder ler o número
    while True:
        numero = str(input(numero_usuario))
        if numero.isnumeric():
            valor = int(numero)
            validacao = True # Se for número, é validado
        else: # Se não for, dá erro e repete até um número ser digitado
            print('ERRO! Digite um número inteiro válido.')
        if validacao: # Se foi validado, sai da repetição e retorna o valor 
            break
    return valor


numero = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {numero}')