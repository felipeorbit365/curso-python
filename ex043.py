peso = float(input('Peso (Kg): '))
altura = float(input('Altura (m): '))
imc = peso / (altura ** 2)

print(f'O IMC referente aos dados fornecidos é {imc:.1f}')

if imc < 18.5: 
    print('Faixa de peso: NORMAL')
elif imc >= 18.5 and imc < 25:
    print('Faixa de peso: IDEAL')
elif imc >= 25 and imc < 30:
    print('Faixa de peso: SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Faixa de peso: OBESIDADE')
else:
    print('Faixa de peso: OBESIDADE MÓRBIDA')
