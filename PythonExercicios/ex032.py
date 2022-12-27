ano = int(input('Digite o ano: '))
if ano % 4 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
### RESOLUÇÃO DO PROFESSOR ###

ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))


### Solução com o Python pegando o ano da máquina ### FEITO PELO PROFESSOR

from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
