# Forma correta: from ex111.utilidadescev import moeda, dado
# De alguma forma que eu não entendi e o Guanabara não explicou, o sistema não reconhece ex111 como diretório
from UtilidadesCeV import moeda # Comentário no YouTube ensinou para VS Code

preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 35, 22)

"""
Comentário no YouTube:

Para quem usa VS Code e não sabe criar pacote :
- Cria uma pasta chamada UtilidadesCeV dentro da pasta ex111, depois crie a pasta Moeda dentro da UtilidadesCeV
- Dentro da pasta Moeda, crie um arquivo manualmente chamado __init__.py
- Para importar, escreva from UtilidadesCev import moeda
"""