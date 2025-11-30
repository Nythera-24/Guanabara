#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
r = float(input('Quantos reais você tem? R$'))
d = r / 5.53
e = r / 6.22
i = r / 0.03639
print(f'Com R${r:.2f} você pode comprar U$ {d:.2f}')
print(f'Com R${r:.2f} você pode comprar € {e:.2f}')
print(f'Com R${r:.2f} você pode comprar ¥ {i:.2f}')
