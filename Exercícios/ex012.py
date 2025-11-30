#Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto.
#p = float(input('Qual o valor do produto? R$ '))
#pr = p * 5 / 100
#d = p - pr
#print(f'O produto que custava R$ {p}, com o desconto de 5% passou a custar R$ {d:.2f}')

#p = float(input('Preço total das peças: R$ '))
#p5 = p * 5 / 100
#p10 = p * 10 / 100
#p12 = p * 12 / 100
#d5 = p - p5
#d10 = p - p10
#d12 = p - p12
#print(f'Com o cupom SKTBR5, sua compra vai de R${p} para: R${d5:.2f} ')
#print(f'Com o cupom SKTBR10, sua compra vai de R$ {p} para: R${d10:.2f}')
#print(f'Com o cupom SKTBR12, sua compra vai de R${p} para: R${d12:.2f}')

#ou

p = float(input('Valor total da compra: R$ '))
d5 = p - (p * 5 / 100)
#ou d5 = p - (p * 0.05)
d10 = p - (p * 10 / 100)
d15 = p - (p * 15 / 100)

print(f'Valor com desconto de 5%: R${d5:.2f} \nValor com desconto de 10%: R${d10:.2f} \nValor com desconto de 15%: R${d15:.2f}')


