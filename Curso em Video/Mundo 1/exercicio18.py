from math import cos,sin,tan,radians
a=float(input('Digite um ângulo: '))
print('O seno de {}° é {:.2f}\nO cosseno de {}° é {:.2f}\nA tangente de {}° é {:.2f}'.format(a,sin(radians(a)),a,cos(radians(a)),a,tan(radians(a))))