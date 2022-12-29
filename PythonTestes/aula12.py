nome = str(input('Qual é seu nome? '))
if nome == 'Otávio':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no Brasil!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminido!')
else:
    print('Seu nome é bem comum!')
print('Tenha um bom dia, {}!'.format(nome))
