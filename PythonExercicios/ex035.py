r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
c1 = (r1 + r2) > r3
c2 = (r1 + r3) > r2
c3 = (r2 + r3) > r1
if c1 == True and c2 == True and c3 == True:
    print('É possível formar um triângulo com essas três retas!')
else:
    print('Não é possível criar um triângulo com as três retas!')
