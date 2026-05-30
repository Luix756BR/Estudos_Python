s = 0
q = 0
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        q +=1
        s += c
print(f'A soma entre todos os {q} números ímpares que são múltiplos de 3 no intervalo de 1 até 500 é {s}')
