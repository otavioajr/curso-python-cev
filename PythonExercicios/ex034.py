salario = float(input('Digite o valor do seu salário: R$'))
if salario > 1250:
    print('Você terá um aumento de 10% e receberá R${:.2f}'.format(salario * 0.1 + salario ))
else:
    print('Você terá um aumento de 15% e receberá R${:.2f}'.format(salario * 0.15 + salario))
### RESOLUÇÃO DO PROFESSOR ###

salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora!'.format(salario, novo))
