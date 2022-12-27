valorCasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos irá pagar a casa? '))
mensal = valorCasa / (anos * 12)

if mensal < (salario * 30 / 100):
    print("""Parabéns! Seu empréstimo foi aprovado.
          Agora você pode adiquirir sua casa própria!!!""")
else:
    print('Infelizmente seu financiamento não foi aprovado!')
