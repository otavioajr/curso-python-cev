from random import randint
num = randint(0, 5)
print('Pensei em um número. Agora adivinhe ele!')
numEsc = int(input('Digite o número: '))
if numEsc == num:
    print('Parabéns, você acertou!')
else:
    print('Número errado, quem sabe na próxima!')
print('O número era {}!'.format(num))