#Mostre o preço de um produto com desconto à vista e e outro preço com juros da máquininha parcelado.
p = float(input('Valor do produto: R$ '))
av5 = p - (p * 0.07)
parcelado = p + (p * 0.05)
print(f'Desconto de 7% para pagamento à vista: R${av5:.2f} \nAcréscimo de 5% de juros para parcelar: R${parcelado:.2f}')