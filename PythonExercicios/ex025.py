nome = str(input('Digite seu nome: '))
nome = nome.upper()
print('SILVA' in nome)


##### RESOLUÇÃO DO PROFESSOR #####

nome = str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))