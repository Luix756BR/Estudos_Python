# Método de fazer o termo da entrada receber a soma dele com a razão a cada fim de iteração
a1 = float(input('Digite o termo inicial dessa PA: '))
r = float(input('Digite a razão dessa PA: '))
for i in range(10):
    print(f'O {i:<2}º termo é {a1:<2}')
    a1 = a1 + r

'''Método de utilizar a própria variável de controle para definir a PA
a1 = int(input('Digite o termo inicial dessa PA: '))
r = int(input('Digite a razão dessa PA: '))
for c in range(a1, (a1 + 9*r) + 1, r):
    print(c)'''