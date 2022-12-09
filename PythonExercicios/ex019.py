from random import choices
a1 = input('Digite o nome do Aluno 1: ')
a2 = input('Digite o nome do Aluno 2: ')
a3 = input('Digite o nome do Aluno 3: ')
a4 = input('Digite o nome do ALuno 4: ')
print('O aluno escolhido foi {}'.format(choices([a1, a2, a3, a4])))
