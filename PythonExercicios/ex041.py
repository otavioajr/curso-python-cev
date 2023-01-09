from datetime import date
anoNasc = int(input('Digite aqui o ano de nascimento: '))
idade = date.today().year - anoNasc
if idade <= 9:
    print('Sua idade é {} e está na categoria MIRIM!'.format(idade))
elif idade <= 14:
    print('Sua idade é {} e está na categoria INFANTIL!'.format(idade))
elif idade <= 19:
    print('Sua idade é {} e está na categoria JUNIOR!'.format(idade))
    elif idade <