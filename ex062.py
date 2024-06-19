print('==============')
print('GERADOR DE PA')
print('==============')

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro_termo
contador = 1
total_termos = 0 
mais_termos = 10 # O programa começa mostrando 10 termos automaticamente

while mais_termos != 0: 
    total_termos = total_termos + mais_termos # Obter toda a quantidade de termos, antes do laço
    while contador <= total_termos:
        print(f'{termo} -> ', end='')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA')
    mais_termos = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total_termos} mostrados.')
