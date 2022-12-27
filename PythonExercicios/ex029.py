vel = int(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Você foi multado!')
    print('O valor da multa é R${:.2f}'.format((vel - 80) * 7))
else:
    print('Parabéns, você está respeitando as regras de transito!')


### RESOLUÇÃO DO PROFESSOR ###

