from random import randint
num = randint(0, 5)
print('Pensei em um número. Agora adivinhe ele!')
numEsc = int(input('Digite o número: '))
if numEsc == num:
    print('Parabéns, você acertou!')
else:
    print('Número errado, quem sabe na próxima!')
print('O número era {}!'.format(num))

### RESOLUÇÃO DO PROFESSOR ###

from random import randint
from time import sleep #importa o timer
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO!!...')
sleep(2) # realiza a espera
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
