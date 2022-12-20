frase = str(input('Digite aqui sua frase: '))
fraseContarA = frase.upper().count('A')
frasePrimeiraPosicaoA = frase.upper().find('A')
fraseUltimaPosicaoA = frase.upper().rfind('A')
print('A letra "A" aparece {} vezes na frase {}'.format(fraseContarA, frase))
print('A primeira letra "A" aparece na posição {} da frase {}'.format(frasePrimeiraPosicaoA, frase))
print('A primeira letra "A" aparece na posição {} da frase {}'.format(fraseUltimaPosicaoA, frase))

print('------------------')
### RESOLUÇÃO DO PROFESSOR ###

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparteceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posiçao {}'.format(frase.rfind('A')+1))
