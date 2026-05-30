from math import factorial
n = int(input('Digite um número para calcular o fatorial: '))
p = 1
while n > 1:
    p *= n
    n -= 1
print(f'O fatorial de {n} é: {p} ')
''' Analogamente, temos outra solução mais simples utilizando a importação da biblioteca math, como se pode ver abaixo:
n = int(input('Digite um número para calcular o fatorial: '))
print(factorial(n))'''
