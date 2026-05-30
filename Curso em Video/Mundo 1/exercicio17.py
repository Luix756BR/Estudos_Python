cateto1 = float(input("Digite o valor do cateto: "))
cateto2 = float(input("Digite o valor do outro cateto: "))

hipotenusa = (cateto1**2 + cateto2**2)(**1/2)

print(f"Os valores dos catetos são {cateto1} e {cateto2}")
print(f"Sua hipotesua é {hipotenusa}")