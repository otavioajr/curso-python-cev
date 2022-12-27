salario = float(input('Digite o valor do seu salário: R$'))
if salario > 1250:
    print('Você terá um aumento de 10% e receberá R${:.2f}'.format(salario * 0.1 + salario ))
else:
    print('Você terá um aumento de 15% e receberá R${:.2f}'.format(salario * 0.15 + salario))
