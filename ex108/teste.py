# Forma correta: from ex108 import moeda
# De alguma forma que eu não entendi e o Guanabara não explicou, o sistema não reconhece ex108 como diretório
import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preco, 10))}') # Passa 10 como parâmetro da taxa
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(preco, 13))}') # Passa 13 como parâmetro da taxa
