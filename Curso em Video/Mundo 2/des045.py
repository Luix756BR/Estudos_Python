from random import choice #Importando o módulo choice da biblioteca random para fazer o computador escolher uma possibilidade aleatória da lista Jokenpô
from time import sleep
Jokenpô = ['Pedra', 'Papel', 'Tesoura']
epc = choice(Jokenpô)
eu = input('Jogue Jokenpô comigo! Digite: Pedra, Papel ou Tesoura\n').strip().lower().title()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
#Definindo as possibilidades de vitória, derrota e empate para cada possibilidade de jogada
if eu == 'Tesoura' and epc == 'Papel':
    print(f'Parabéns você me venceu, eu joguei {epc} e você jogou {eu}')
elif eu == 'Tesoura' and epc == 'Pedra':
    print(f'Infelizmente, você perdeu, eu joguei {epc} e você jogou {eu}')
elif eu == 'Tesoura' and epc == 'Tesoura':
    print(f'Eita! Nós empatamos, eu joguei {epc} e você jogou {eu}')
elif eu == 'Pedra' and epc == 'Tesoura':
    print(f'Parabéns você me venceu, eu joguei {epc} e você jogou {eu}')
elif eu == 'Pedra' and epc == 'Papel':
    print(f'Infelizmente, você perdeu, eu joguei {epc} e você jogou {eu}')
elif eu == 'Pedra' and epc == 'Pedra':
    print(f'Eita! Nós empatamos, eu joguei {epc} e você jogou {eu}')
elif eu == 'Papel' and epc == 'Pedra':
    print(f'Parabéns você me venceu, eu joguei {epc} e você jogou {eu}')
elif eu == 'Papel' and epc == 'Tesoura':
    print(f'Infelizmente, você perdeu, eu joguei {epc} e você jogou {eu}')
elif eu == 'Papel' and epc == 'Papel':
    print(f'Eita! Nós empatamos, eu joguei {epc} e você jogou {eu}')
else:
    print('COMANDO INVÁLIDO!')