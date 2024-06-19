ano = int(input('Insira o ano que deseja analisar: '))

# Anos bissextos são uniformemente divisíveis por 100 e 400.
# Um ano bissexto tem que ser divisível por 4, porém, a regra para anos centenários é que seja divisível por 400.

# SE o ano for divisível por 4 E SE não for divisível por 100, é bissexto.
# OU SE for divisível por 400, é bissexto. Outro critério, ignorando as duas primeiras condições.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))

"""
Para ser bissexto, o ano deve ser:

Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;

Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;

Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, com o resto igual a zero.

Ou seja, para anos bissextos:
- Se for uma divisão exata em relação a 4, verifica se não é divisível por 100. Se não for, é bissexto.
- Se não for divisível por 4, verifica se é divisível por 400. Se não for, não é bissexto.
- Se não for divisível por 4, verifica se é divisível por 400. Se for, é bissexto. 

São bissextos os anos múltiplos de 400, exceto se for múltiplo de 100, mas não de 400.

Comentário no YouTube que ajuda a entender: 

"ano % 4 == 0" diz que todos os anos divisíveis por 4 são bissextos (2008, 2012, 2016, 2020 etc)
"ano % 100 != 0" diz que todos os anos divisíveis por 100 NÃO são bissextos, criando "falhas" na sequência (retira-se os anos 1700, 1800, 1900, 2000 etc)
"ano % 400 == 0" preenche as falhas com somente os números divisíveis por 400 (800, 1200, 1600, 2000 etc)
Então "ano % 4 == 0 and ano % 100 != 0" é um critério, e "ano % 400 == 0" é outro.

"""
