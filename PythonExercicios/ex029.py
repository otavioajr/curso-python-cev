vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Você foi multado!')
    print('O valor da multa é R${:.2f}'.format((vel - 80) * 7))
else:
    print('Parabéns, você está respeitando as regras de transito!')


### Resolução do Professor ###

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')
