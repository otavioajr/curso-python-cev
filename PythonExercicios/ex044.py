print('Os produtos que temos a venda são: geladeira, tv e celular!')
print('O que deseja comprar?')
produto = str(input())
print('=-'*20)
print('''Os pagamentos em dinheiro ou cheque a vista tem 10% de desconto!
         Os pagamentos à vista no cartão tem 5% de desconto!
         Os pagamentos em até 2x não é possível conceder o desconto!
         Os pagamentos em 3x ou mais há um acréscimo de 20% de juros!''')
geladeira = 4500.50
tv = 5650
celular = 3890.99
if produto == 'geladeira':
    print('O valor é {}'.format(geladeira))
    pagamento = str(input('Qual a forma de pagamento? '))
    