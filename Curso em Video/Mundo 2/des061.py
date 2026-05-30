a1 = float(input('A1: '))
r = float(input('Razão: '))
n = 1
while n <=10:
    print(f'{n:>2}º termo: {a1:<2.2f}')
    a1 += r
    n += 1

