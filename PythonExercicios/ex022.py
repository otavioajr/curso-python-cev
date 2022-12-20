nome = str(input('Digite aqui seu nome: '))
dividido = nome.split()
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('A quantidade de caracteres que seu nome tem é {} letras'.format(len(''.join(dividido))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(dividido[0], len(dividido[0])))

# Resolução do professor

nome = str(input('Digite aqui seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primneiro nome é {} e tem ao todo {} letras'.format(separa[0], len(separa[0])))
