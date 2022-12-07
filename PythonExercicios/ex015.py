dias = int(input('Digite a quantidade de dias utilizados: '))
km = float(input('Digite a quantidade de km percorrido: '))
print('O total a pagar é R${:.2f}'.format((dias * 60) + (km * 0.15)))