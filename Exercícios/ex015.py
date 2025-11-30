#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
#km = float(input('Quantos Km foram percorridos? '))
#d = float(input('Por quantos dias alugou o carro? '))
#pd = d * 60
#r = km * 0.15
#soma = pd + r
#print(f'O valor total do aluguel é de: R${soma:.2f}')

#Ou

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
soma = (dias * 60) + (km * 0.15)
print(f'O total a ser pago é R$: {soma:.2f}')

