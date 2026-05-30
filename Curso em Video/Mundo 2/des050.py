s = 0
for i in range(6):
    n = int(input(f'Digite o {i+1}º número: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos inteiros digitados que são pares é igual a: {s}')