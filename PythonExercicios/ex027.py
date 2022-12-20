nome = str(input('Digite aqui seu nome: '))
nomeDividido = nome.split()
tamanhoLen = len(nomeDividido)
print('Primeiro nome: {}'.format(nomeDividido[0]))
print('Último nome: {}'.format(nomeDividido[tamanhoLen - 1]))

print('---------------')
### Resolução do professor ###

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome) - 1]))
