largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = altura * largura
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m².'.format(largura, altura, area))
litro_tinta = area / 2
print('Para pintar essa parede, você precisará de {:.4f}l de tinta'.format(litro_tinta))

