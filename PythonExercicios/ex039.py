idade = int(input('Digite aqui sua idade: '))
if idade < 18:
    falta = 18 - idade
    print('Você não tem a idade mínima para se alistar, faltam {} anos para se alistar!'.format(falta))
elif idade > 18:
    falta = idade - 18
    print('Você já passou {} anos do alistamento!'.format(falta))
else:
    print('Você já tem a idade mínima para se alistar!')
