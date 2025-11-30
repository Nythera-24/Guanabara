#Pergunte a medida em metros e mostre o equivalente em km, hm (hequitômetros), dam (decâmetros), dm (decímetros), cm e mm
m = float(input('Uma distância em metros: '))
print(f'A medida de {m} corresponde a: ')
print(f'{m / 1000:.3f}km')
print(f'{m / 100:.2f}hm')
print(f'{m / 10:.1f}dam')
print(f'{m * 10:.0f}dm')
print(f'{m * 100:.0f}cm')
print(f'{m * 1000:.0f}mm')


