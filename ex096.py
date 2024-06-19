def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area_terreno}m²')


print('Controle de Terrenos')
print('--------------------')
area_largura = float(input('LARGURA (m): '))
area_comprimento = float(input('COMPRIMENTO (m): '))

area(area_largura, area_comprimento)
