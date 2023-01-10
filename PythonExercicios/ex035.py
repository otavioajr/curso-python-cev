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
### RESOLUÇÃO DO PROFESSOR ###

print('-=' * 20)
print('Analisador de Triângulo')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
