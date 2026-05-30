a1 = 0
a2 = 1
a3 = a1 + a2
n = int(input('Quantos termos da sequência de Fibonacci quer? '))
for c in range(n):
    if c == 0:
        print(a1, end=' --> ')
    elif c == 1:
        print(a2, end=' --> ')
    else:
        if c == n:
            print(a3, end=' --> ')
            a2seg = a3
            a3 += a2
            a2 = a2seg
            
    

        
