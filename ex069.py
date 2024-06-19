maiores_idade = 0
total_homens = 0
mulheres_novas = 0

while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': # Enquanto não digitar 'M' ou 'F', repete
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18: 
        maiores_idade = maiores_idade + 1
    if sexo == 'M':
        total_homens = total_homens + 1
    if sexo == 'F' and idade < 20:
        mulheres_novas = mulheres_novas + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('--- FIM DO PROGRAMA ---')
print(f'Total de pessoas com mais de 18 anos: {maiores_idade}')
print(f'Ao todo temos {total_homens} homens cadastrados')
print(f'E temos {mulheres_novas} mulheres com menos de 20 anos')
