#Método 1 utilizando if, checando todas as iterações
print(f'Os números pares no intervalo entre 1 e 50 são:',end=' ')
for c in range(1,51):
    if c % 2 == 0:
        print(c,'',end='')

'''Método 2 utilizando passo 2 para fazer menos iterações, o que vai exigir menos do computador
print(f'Os números pares no intervalo entre 1 e 50 são:',end=' ')
for c in range(2,51,2):
    print(c,'',end='')'''
