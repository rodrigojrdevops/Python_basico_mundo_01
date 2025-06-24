larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede possui a dimensão de {:.2f}m² x {:.2f}m de altura e a sua área total é de {:.2f}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {:.2f} litros de tinta.'.format(tinta))
