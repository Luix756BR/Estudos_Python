from random import randint
pc = randint(0,10)
qtdp = 0
print(f'{'-='*25}\nTente advinhar o número de 1 a 10 que eu pensei!\n{'-='*25}')
p = int(input('Dê seu palpite: '))
while p != pc:
    print('Errado! Você não acertou, tente novamente')
    p = int(input('Dê seu palpite: '))
    qtdp += 1
print(f'Você acertou, eu pensei no número {pc} e você precisou de {qtdp + 1} palpites para acertar')

