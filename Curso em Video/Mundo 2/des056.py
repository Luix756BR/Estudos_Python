maior = menor = soma = qtdm = 0
nomev = ''
for c in range(1,5):
    sexo = input(f'Qual o sexo da {c}º pessoa (M/F)? ')
    if sexo == 'M':
        nome = input(f'Qual o nome da {c}º pessoa? ').strip()
        idade = int(input(f'Qual a idade da {c}º pessoa? '))
        if idade == maior:
            nomev = 'Os homens tem a mesma idade'
        if maior == 0 or idade > maior:
            maior = idade
            nomev = nome
        soma += idade
    if sexo == 'F':
        nome = input(f'Qual o nome da {c}º pessoa? ')
        idade = int(input(f'Qual a idade da {c}º pessoa? '))
        soma += idade
        if idade < 20:
            qtdm += 1
print(f'A média de idade do grupo é: {soma/c} anos\nO nome do homem mais velho é: {nomev}\nA quantidade de mulheres com menos de 20 anos é: {qtdm}')
