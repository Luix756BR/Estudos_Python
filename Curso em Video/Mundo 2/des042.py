#Verificação de desigualdade triângular e tipo de triângulo
r1 = float(input('Informe o comprimento da 1° reta: '))
r2 = float(input('Informe o comprimento da 2° reta: '))
r3 = float(input('Informe o comprimento da 3° reta: '))
tipot = '0'
#Primeiramente, verificaremos o tipo do triângulo
if r1 == r2 and r1 == r3:
    tipot = 'Equilátero'
elif r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r3 == r2 and r3 != r1:
    tipot = 'Isósceles'
elif r1 != r2 and r1 != r3 and r3 != r2:
    tipot = 'Escaleno'
#Feito isto, agora vamos fazer a verificação da desigualdade triângular e printar o tipo do triângulo
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'Essas retas podem formar um triângulo {tipot}')
else:
    print('Essas retas não podem formar um triângulo')

