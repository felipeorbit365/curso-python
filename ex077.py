palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras: # Percorre cada uma das palavras no laço
    print(f'\nNa palavra {palavra.upper()} temos ', end='') # Cada vez que começa, quebra a linha e escreve o restante
    for letra in palavra: # Para cada letra nas palavras, faz verificações
        if letra.upper() in 'AEIOU': # Verifica se a letra (convertida para maiúscula) é uma vogal
            print(letra.upper(), end='') # A letra é escrita, já que é vogal, em maiúsculas

"""
Tem um for dentro do outro
O primeiro for analisa cada elemento da tupla, de aprender até futuro
Por ser uma listagem, é possível fazer um outro for que analisa cada letra na palavra da vez
Se fizer parte do grupo das vogais, 'aeiou', é exibido
"""
