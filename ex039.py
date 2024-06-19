from datetime import date 

ano_atual = date.today().year
ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade < 18: 
    prazo = 18 - idade
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')
    print(f'Ainda falta(m) {prazo} ano(s) para seu alistamento.')
    print(f'Seu alistamento será em {ano_atual + prazo}.')
elif idade == 18: 
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')
    print(f'Faça seu alistamento ao serviço militar ainda esse ano se ainda não o fez.')
else:
    prazo = idade - 18
    print(f'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')
    print(f'Se ainda não se alistou, você já deveria ter se alistado há {prazo} ano(s).')
    print(f'Se já se alistou, seu alistamento foi em {ano_atual - prazo}.')
