km = float(input('Digite a distância da viagem: '))
if km > 200:
    preco = km * 0.45
    print('O preço de sua viagem será R${:.2f}'.format(preco))
else:
    preco = km * 0.5
    print('O preço de sua viagem será R${:.2f}'.format(preco))
print('Boa viagem!!!')


### SOLUÇÃO DO PROFESSOR ###

distancia = float(input('Qual a distância de sua viagem? '))
print(' Você está prestes a começar uma viagem de {}km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço de sua passagem será {:.2f}'.format(preco))


### MÉTODO SIMPLIFICADO DO PROFESSOR ###

distancia = float(input('Qual a distância de sua viagem? '))
print(' Você está prestes a começar uma viagem de {}km.'.format(distancia))
preco = distancia *0.50 if distancia <= 200 else distancia * 0.45
print('E o preço de sua passagem será {:.2f}'.format(preco))