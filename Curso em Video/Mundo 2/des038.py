#Verificar dois números inteiros e dizer qual é o maior
n1 = int(input('Informe o valor do 1° número: '))
n2 = int(input('Informe o valor do 2° número: '))
if n2 == n1:
    print('Não existe valor maior, os dois são iguais')
elif n1 > n2:
    print(f'O primeiro valor ({n1}) é maior')
else:
    print(f'O segundo valor ({n2}) é maior')