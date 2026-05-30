from datetime import date
y = date.today().year
maior = 0
menor = 0
for c in range(7):
    a = int(input('Ano de nascimento: '))
    i = y - a
    if i >= 21:
        maior += 1
    else:
        menor += 1
print(f'No ano de {y}, há {maior} pessoas de maior e {menor} pessoas de menor')