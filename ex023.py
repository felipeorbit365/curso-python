numero = int(input('Informe um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

# UDCM = Unidade Dezena Centena Milhar
# Pegar um número, fazer a divisão inteira dele por 1 e depois realizar o módulo,
# o resto da divisão, por 10 sempre vai pegar o último número dele
# O resto é o que sobrou. O número depois da vírgula.
# Aumentar o número da visão inteira faz a vírgula andar, assim, permitindo movimentar
# entre as casas MCDU
# O módulo por 10 faz pegar só o último dígito
# O número que realiza a divisão segue o padrão de unidade, dezena, centa e milhar
# 1, 10, 100, 1000