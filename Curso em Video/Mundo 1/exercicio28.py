from random import randint
n = randint(0,5)
print('-='*10)
print('PROGRAMA DE ADIVINHAÇÃO')
print('-='*10)
print(n)
u = int(input('Tente adivinhar o número em que eu pensei: '))
if u == n:
    print('Parabéns! Você adivinhou corretamente!')
else:
    print('Errado! Infelizmente você não obteve êxito em descobrir o número em que pensei')