s = float(input('Digite o valor do seu salário: '))
if s > 1250:
    print(f'Para salários acima de R${s}, há um aumento de 10%\nLogo seu novo salário será de R${s*(110/100):.2f}')
else:
    print(f'Para salários iguais ou abaixo de R${s}, há um aumento de 15%\nLogo seu novo salário será de R${s*(115/100):.2f}')