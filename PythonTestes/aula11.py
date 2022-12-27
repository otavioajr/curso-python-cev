a = 3
b = 5
print('Ps valores são \033[32;44m{}\033[m e \033[31;44m{}\033[m!!!'.format(a, b))


####################

nome = 'Otávio'
print('Olá! Muito prazer te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))


####################

nome = 'Otávio'
cores = {'limpa': '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7:30m'}
print('Olá! Muito prazer te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome, cores['limpa']))