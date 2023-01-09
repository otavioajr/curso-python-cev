nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua média é {} e, você foi REPROVADO!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média é {} e, você está de RECUPERAÇÃO!'.format(media))
else:
    print('Sua média é {} e, você foi APROVADO!'.format(media))
