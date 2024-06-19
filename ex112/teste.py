# Forma correta: from ex112.utilidadescev import moeda, dado
# De alguma forma que eu não entendi e o Guanabara não explicou, o sistema não reconhece ex112 como diretório
from UtilidadesCeV import moeda 
from UtilidadesCeV import dado

preco = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 35, 22)
