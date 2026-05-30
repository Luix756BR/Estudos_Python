n = int(input('Digite um número inteiro: '))
b = int(input('''Escolha a base de conversão desse inteiro
[1] Binária
[2] Octal
[3] Hexadecimal\n'''))
if b == 1:
    print(bin(n)[2:])
elif b == 2:
    print(oct(n)[2:])
elif b == 3:
    print(hex(n)[2:])
else:
    print('Você não escolheu uma base de conversão')

