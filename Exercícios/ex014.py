#Faça um programa que leia a temperatura em Celsius e faça a conversão para Fahrenheit e Kelvin.
c = float(input('Qual é a temperatura em Cº? '))
k = c + 273.15
f = 32 + (c * 1.8)
print(f'Conversão de Celsius para Fahrenheit: {f:.1f}ªF \nConversão de Celsius para Kelvin {k:.2f}')
