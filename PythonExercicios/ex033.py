n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
r1 = n1 > n2
r2 = n2 > n3
if r1 == True and r2 == True:
    print('O número {} é o maior entre os três.'.format(n1))
if r1 == False and r2 == True:
    print('O número {} é o maior entre os três.'.format(n2))
if r1 == False and r2 == False:
    print('O número {} é o maior entre os três.'.format(n3))
### RESOLUÇÃO DO PROFESSR ###

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {} e o maior foi {}'.format(menor, maior))
