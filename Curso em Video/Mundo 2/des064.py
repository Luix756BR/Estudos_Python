n = int(input('Informe um número inteiro ou 999 para finalizar: '))
soma = n
q = 1
if n == 999:
    None
else:
    while n != 999:
        n = int(input('Informe um número inteiro ou 999 para finalizar: '))
        if n == 999:
            None
        else:
            q += 1
            soma += n
    if q == 1:
        print(f'Apenas o número {soma} foi digitado')
    else:
        print(f'Foram digitados {q} números e a soma entre eles vale {soma}')
        

