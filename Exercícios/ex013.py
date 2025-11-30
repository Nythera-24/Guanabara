#Faça um programa que leia o salário de um funcionário e então reajuste o salário com 15% a mais no valor.
s = float(input('Qual é o salário do funcionário?: R$ '))
r = s + (s * 0.15)
#ou
#r = s + (s * 15 / 100)
print(f'Com o ajuste de 15%, o salário passa de R$ {s:.2f} para: R$ {r:.2f}')



