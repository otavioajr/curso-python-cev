km = float(input('Digite a distância da viagem: '))
if km > 200:
    preco = km * 0.45
    print('O preço de sua viagem será R${:.2f}'.format(preco))
else:
    preco = km * 0.5
    print('O preço de sua viagem será R${:.2f}'.format(preco))
print('Boa viagem!!!')
