peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é {} e você esta ABAIXO DO PESO!'.format(imc))
elif imc < 25:
    print('Seu IMC é {} e você esta no PESO IDEAL!'.format(imc))
elif imc < 30:
    print('Seu IMC é {} e você esta com SOBREPESO!'.format(imc))
elif imc < 40:
    print('Seu IMC é {} e você esta OBESO!'.format(imc))
else:
    print('Seu IMC é {} e você esta com OBESIDADE MORBIDA!'.format(imc))
