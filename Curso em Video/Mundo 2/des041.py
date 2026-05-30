from datetime import date
y = date.today().year
a = int(input('Informe o ano de nascimento do atleta: '))
i = (y - a)
if i < 0:
    print('Insira um ano válido')
elif i <= 9:
    print('MIRIM')
elif i > 9 and i<=14:
    print('INFANTIL')
elif i > 14 and i <= 19:
    print('JUNIOR')
elif  i == 20:
    print('SÊNIOR')
else:
    print('MASTER')
