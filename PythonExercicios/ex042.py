print('-='*20)
print('Analisador de Triângulo')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\n Os segmentos acima PODEM FORMAR um triângulo! \n')
    print('=-='*20)
    if r1 == r2 and r1 == r3:
        print('O triângulo possui todos os lados iguais formando um TRIÂNGULO EQUILÁTERO! \n')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo possui apenas dois lados iguais formando um TRIÂNGULO ISÓCELES \n')
    else:
        print('O triângulo possui todos os lados diferentes formando um TRIÂNGULO ESCALENO! \n')
else:
    print('\n Os segmentos acima NÃO PODEM FORMAR um triângulo!')
