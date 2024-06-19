# Forma correta: from ex107 import moeda
# De alguma forma que eu não entendi e o Guanabara não explicou, o sistema não reconhece ex107 como diretório
import moeda

preco = float(input('Digite o preço: R$'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preco, 10)}') # Passa 10 como parâmetro da taxa
print(f'Reduzindo 13%, temos {moeda.diminuir(preco, 13)}') # Passa 13 como parâmetro da taxa
