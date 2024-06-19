primeiro = float(input('Primeiro segmento: '))
segundo = float(input('Segundo segmento: '))
terceiro = float(input('Terceiro segmento: '))

if primeiro < (segundo + terceiro) and segundo < (primeiro + terceiro) and terceiro < (primeiro + segundo):
    print(f'Os segmentos acima PODEM formar um triângulo ', end='')
    if primeiro == segundo == terceiro:
        print('EQUILÁTERO')
    elif primeiro == segundo or segundo == terceiro or primeiro == terceiro:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo.')

''' 
Para três segmentos fecharem um triângulo, cada lado deve ser menor que a soma dos outros dois.
Cada um dos segmentos têm que ser menor do que a soma do comprimento dos outros dois.
Equilátero: Todos os lados iguais
Isósceles: Dois lados iguais
Escaleno: Todos os lados diferentes

---
,end='' -> No fim da linha não vai ser nada, não vai ter Enter, quebra de linha.
---

Lógica de igualdade e diferença

Igualdade
- Se uma coisa A que é igual a B que é igual a C, pode-se afirmar que A é igual a C. A igualdade é inclusiva.
- Logo, é possível representar: A == B == C

Na diferença, isso não ocorre

Diferença
- A pode ser diferente de B, B pode ser diferente de C, mas A pode ser igual a C
- Logo, não é possível representar: A != B != C
- O correto é: A != B != C != A

---

No exercício 42, um bloco do if está dentro de outro bloco do if. É uma condição aninhada. 

'''