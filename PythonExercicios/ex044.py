print('Os produtos que temos a venda são: geladeira, tv e celular!')
print('O que deseja comprar?')
produto = str(input())
print('Qual o valor do produto?')
valor_produto = float(input())
print('=-'*20)
print('''Os pagamentos em dinheiro ou cheque a vista tem 10% de desconto!
         Os pagamentos à vista no cartão tem 5% de desconto!
         Os pagamentos em até 2x não é possível conceder o desconto!
         Os pagamentos em 3x ou mais há um acréscimo de 20% de juros!''')
print('=-'*20)
print('Qual a forma de pagamento?')
pagamento = str(input())
print('=-'*20)
if pagamento == 'dinheiro' or 'cheque':
    preco = valor_produto - (valor_produto * 0.1)
    print('Sua compra à vista vai custar R${}'.format(preco))
elif pagamento == 'cartao' or 'cartão':
    preco = valor_produto - (valor_produto * 0.05)
    print('Sua compra à vista no cartão vai custar R${}'.format(preco))


#elif pagamento == 'parcelado':
#    print('Em quantas vezes irá parcelar?')
#    pagamento_parcelado = int(input())
#    if pagamento_parcelado > 2:
#        preco = valor_produto + (valor_produto * 0.2)
#        print('Sua compra com {} parcelas fica no total de R${}. Com cada parcela custando R${}'.format(pagamento_parcelado, preco, (preco/pagamento_parcelado)))