#Desigualdade triangular.
r1 = float(input('Digite o comprimento da 1º reta: '))
r2 = float(input('Digite o comprimento da 2º reta: '))
r3 = float(input('Digite o comprimento da 3º reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Essas retas podem formar um triângulo')
else:
    print('Essas retas não podem formar um triângulo')