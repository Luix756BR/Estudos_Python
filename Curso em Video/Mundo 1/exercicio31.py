d = float(input('Qual a distância da sua viagem? '))
if d > 200:
    print(f'Para uma viagem de {d}km, cobramos 0,45 por km, logo sua viagem custa: R${d*0.45:.2f}')
else:
    print(f'Para uma viagem de {d}km, cobramos 0,50 por km, logo sua viagem custa: R${d*0.5:.2f}')