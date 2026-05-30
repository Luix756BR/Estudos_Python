from datetime import date
a = input('Digite um ano(se quiser analisar o ano atual, digite atual): ')
if a == 'atual':
    a = date.today().year
if int(a) % 4 == 0 and int(a) % 100 != 0 or int(a) % 100 == 0 and int(a) % 400 == 0:
    print(f'O ano de {a} é bissexto')
else:
    print(f'O ano de {a} não é bissexto')