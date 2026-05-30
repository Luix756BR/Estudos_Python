n = int(input('Digite um número inteiro: '))
maior = menor = soma = n
q = cig = 1

escolha = input('Quer inserir mais valores? [S/N] ')
while escolha not in 'SsNn':
    print('\033[31mOpção inválida!\033[0m Digite novamente')
    escolha = input('Quer inserir mais valores? [S/N] ')
if escolha in 'Nn':
    print(f'Apenas o valor {n} foi inserido')
else:
    while escolha in 'Ss':
        n = int(input('Digite um número inteiro: '))
        soma += n
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
        else:
            cig += 1
        q += 1
        while escolha not in 'SsNn':
            print('\033[32mOpção inválida!\033[0m')
            escolha = input('Quer inserir mais valores? [S/N] ')
    if cig == q:
        print('Os valores inseridos foram todos iguais')
    elif cig < q:
        print(f'O maior número inserido foi {maior} e o menor foi {menor}\nA média entre os números inseridos vale {soma/q}')