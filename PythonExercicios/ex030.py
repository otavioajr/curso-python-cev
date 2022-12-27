num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é ímpar!'.format(num))


#### MÉTODO IF SIMPLIFICADO ### FEITO POR MIM

num = int(input('Digite um número: '))
print('O número {} é par!'.format(num) if num % 2 == 0 else 'O número {} é ímpar!'.format(num))


### Solução do professor ###

numero = int(input('Digite um número qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('Onúmero {} é ÍMPAR'.format(numero))
