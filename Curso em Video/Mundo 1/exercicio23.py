n = int(input('Digite um número:'))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('unidade de milhar: {}'.format(m))
#Com string 
n = (input('Digite um número:')).strip()
r = n.rjust(4, '0')
print('unidade: {}'.format(r[3]))
print('dezena: {}'.format(r[2]))
print('centena: {}'.format(r[1]))
print('unidade de milhar: {}'.format(r[0]))