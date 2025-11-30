l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
m2 = l * a
t = m2 / 2
print(f'Sua parede tem a dimensão de {l}x{a} e sua área é de {m2:.2f}m².')
print(f'Para pintar essa parede, você precisará de {t}l de tinta.')
