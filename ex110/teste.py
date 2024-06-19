# Forma correta: from ex110 import moeda
# De alguma forma que eu não entendi e o Guanabara não explicou, o sistema não reconhece ex110 como diretório
import moeda

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 20, 12)
