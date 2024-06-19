def leiaInt(mensagem):
    while True:
        try:
            numero_usuario = int(input(mensagem))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número inteiro válido.')
            continue # Continua no laço
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar o número.')
            return 0 # Um  valor padrão para que funcione a análise
        else:
            return numero_usuario
        

def leiaFloat(mensagem):
    while True:
        try:
            numero_usuario = float(input(mensagem))
        except (ValueError, TypeError):
            print('ERRO! Por favor, digite um número inteiro válido.')
            continue # Continua no laço
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar o número.')
            return 0 # Um  valor padrão para que funcione a análise
        else:
            return numero_usuario


numero_inteiro = leiaInt('Digite um Inteiro: ')
numero_real = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {numero_inteiro} e o real foi {numero_real}')
