km = float(input('Digite a velocidade do carro: '))
if km > 80:
    print('Você será multado e o valor da sua multa será de R${:.2f}'.format((km - 80)*7))
else:
    print('Fique à vontade')