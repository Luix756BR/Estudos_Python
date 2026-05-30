q = cig = 1
n = int(input('Informe um número inteiro: '))
maior = menor = soma = n
escolha = input('Quer continuar inserindo valores? [S/N] ').strip()
if escolha in 'Nn':
    print(f'Apenas o número {n} foi inserido')
else:
    while escolha in 'sS':
        n = int(input('Informe um número inteiro: '))
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
        else:
            cig += 1
        soma += n
        q += 1
        escolha = input('Quer continuar inserindo valores? [S/N] ').strip()
    if cig == q:
        print('Os valores lidos são todos iguais')
    else:
        print(f'{maior} foi o maior lido, {menor} foi o menor valor lido e a média entre eles vale {soma/q:.2f}')
    

