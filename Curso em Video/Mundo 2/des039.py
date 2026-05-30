from datetime import date
y = date.today().year
d = int(input('Qual o ano nascimento do jovem? '))
if (y - d) == 18:
    print(f'Está na hora deste jovem se alistar em {y}')
elif (y - d) < 18 and 18 - (y - d) == 1:
    print(f'Ainda está cedo, este jovem só se alistará daqui a {18 - (y - d)} ano em {y + (18 - (y - d))}')
elif (y - d) < 18:
    print(f'Ainda está cedo, este jovem só se alistará daqui a {18 - (y - d)} anos em {y + (18 - (y - d))}')
elif (y - d) > 18 and (y - d) - 18 == 1:
    print(f'O tempo de alistamento já passou, este jovem deveria ter se alistado há {(y - d) - 18} ano em {y - ((y - d) - 18)} ')
elif (y - d) > 18:
    print(f'O tempo de alistamento já passou, este jovem deveria ter se alistado há {(y - d) - 18} anos em {y - ((y - d) - 18)} ')
