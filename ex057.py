sexo_usuario = str(input('Informe seu sexo [M/F]: ')).upper()

while sexo_usuario != 'M' and sexo_usuario != 'F':
    sexo_usuario = str(input('Dados inválidos. Por favor, insira seu sexo [M/F]: '))
print(f'Sexo {sexo_usuario} registrado com sucesso!')

"""
Comentário no YouTube explicando a diferença entre OR e AND:

Eu fiz -> while sexo != 'M' or sexo != 'F': 
e Meu loop não tava parando nunca, nem colocando M ou F, achei muito estranho e demorei pra entender o motivo. 
A minha maneira de interpretar pra entender melhor foi a seguinte: 
'Enquanto sexo for diferente de 'M' OU diferente de 'F' entre na repetição', 
so que 'M' sempre será diferente de 'F' e vise versa. 
Então se digitasse 'M' o programa testava --> 'M' é diferente de 'M' OU de 'F' ? Sim , 'M' é igual a 'M' , 
porém é diferente de 'F', então entre na repetição! ,
 e se digitasse 'F' ele testava --> 'F' é diferente de 'M' OU de 'F' ? Sim, 'F' é diferente de 'M' ,
entre na repetição! E digitando qualquer palavra OU um OU outro sempre seriam satisfeitos, loop infinito! 

Usando a função AND da certo porque enquanto sexo for diferente de "M" E de "F" ele entra no loop. 
Qualquer palavra então vai fazer ele entrar na repetição, 
porém se você digitar 'M' ele vai testar -> 'M' É diferente de M e F ? não, é só diferente de F e igual a M, 
saia da repetição.  Se colocar 'F' ele vai testar -> É diferente de M e F? não, é só diferente de M e igual a F, 
saia da repetição. Acho que é isso

---

Resolução do Guanabara:
O Guanabara fez remoção de espaços e fatiamento para epgar somente a primeira letra
Também utilizou " not in 'MmFf' "
"""
