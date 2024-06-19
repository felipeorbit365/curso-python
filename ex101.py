def voto(ano_nascimento): 
    from datetime import date # Escopo de importação 
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 65: # Se idade é ao mesmo tempo maior ou igual a 16 e menor que 18 OU maior que 65
        return f'Com {idade} anos: VOTO OPCIONAL'
    else: # Entre 18 e 65
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


ano_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_nascimento))

"""  
Jeito que eu fiz:

from datetime import date 

def voto(ano_nascimento): 
    if idade >= 18 and idade < 75:
        return 'VOTO OBRIGATÓRIO'
    if idade < 18:
        return 'VOTO NEGADO'
    if idade >= 75:
        return 'VOTO OPCIONAL'


ano_atual = date.today().year
ano_nascimento = int(input('Em que ano você nasceu? '))
idade = ano_atual - ano_nascimento

tipo_voto = voto(ano_nascimento)
print(f'Com {idade} anos: {tipo_voto}')

---

Jeito colocando o número manualmente:

Exemplo - 2003
-> print(voto(2003))
""" 