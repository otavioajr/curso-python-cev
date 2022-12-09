import math
angulo = float(input('Digite o ângula a ser calculado: '))
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))
