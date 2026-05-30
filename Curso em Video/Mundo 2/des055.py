
maior = 0
menor = 0
for c in range(5):
    p = int(input(f'Informe o peso da {c+1}º pessoa: '))
    if maior == 0 or p > maior:
        maior = p
    if menor == 0 or p < menor:
        menor = p
print(f'O maior peso lido foi de {maior}kg e o menor foi de {menor}kg')