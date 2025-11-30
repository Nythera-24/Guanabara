def somapeso(p1, p2, p3):
    return p1 + p2 + p3

nome = str(input('Digite seu nome: '))
peso = float(input('Qual seu peso? '))
peso2 = float(input('Qual o peso da sua mãe? '))
peso3 = float(input('Qual o peso do seu amigo? '))
s = somapeso(peso, peso2, peso3)
print('Olá, {}! \nO peso somado de vocês é {:.2f}kg'.format (nome, s))
print('O elevador comporta até 400kg \nSendo assim, ainda tem a capacidade de: {:.2f}kg!'.format(400 - s))

