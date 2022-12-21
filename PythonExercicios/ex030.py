num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é ímpar!'.format(num))


#### MÉTODO IF SIMPLIFICADO ### FEITO POR MIM

num = int(input('Digite um número: '))
print('O número {} é par!' if num % 2 == 0 else 'O número {} é ímpar!'.format(num))