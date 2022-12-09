from random import choice
a1 = input('Digite o nome do Aluno 1: ')
a2 = input('Digite o nome do Aluno 2: ')
a3 = input('Digite o nome do Aluno 3: ')
a4 = input('Digite o nome do Aluno 4: ')
lista = [a1, a2, a3, a4]
print('O aluno escolhido foi {}'.format(choice(lista)))
