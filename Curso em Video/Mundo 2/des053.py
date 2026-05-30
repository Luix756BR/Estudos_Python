t = input('Digite a frase: ').strip().lower().split()
t = ''.join(t)
l = len(t)
i = ''
for c in range(l - 1,-1,-1):
    i += t[c]
if i == t:
    print('Esta frase é um palíndromo')
else:
    print('Esta frase não é um palíndromo')