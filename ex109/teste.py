# Forma correta: from ex109 import moeda
# De alguma forma que eu não entendi e o Guanabara não explicou, o sistema não reconhece ex109 como diretório
import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10, True)}') # Passa 10 como parâmetro da taxa
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13, True)}') # Passa 13 como parâmetro da taxa
