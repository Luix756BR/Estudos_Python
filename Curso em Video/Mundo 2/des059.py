n1 = float(input('Informe o valor do 1º número: '))
n2 = float(input('Informe o valor do 2º número: '))
print(''' 
        [ 1 ]somar
        [ 2 ]multiplicar
        [ 3 ]maior
        [ 4 ]novos números
        [ 5 ]sair do programa\n''')
escolha = int(input('Escolha uma opção: '))
while escolha != 5:
    if escolha == 1:
        print(f'\033[32mA soma entre {n1} e {n2} é {n1+n2}\033[m')
    elif escolha == 2:
        print(f'\033[32mO produto entre {n1} e {n2} é {n1*n2}\033[m')
    elif escolha == 3:
        maior = n1 
        if n2 > n1:
            maior = n2
        print(f'\033[32mO maior entre {n1} e {n2} é {maior}\033[m')
    elif escolha == 4:
        n1 = float(input('\nInforme o valor do 1º número: '))
        n2 = float(input('Informe o valor do 2º número: '))
    else:
        print('Comando inválido, escolha uma das opções descritas')
    print(''' 
        [ 1 ]somar
        [ 2 ]multiplicar
        [ 3 ]maior
        [ 4 ]novos números
        [ 5 ]sair do programa\n''')
    escolha = int(input('Escolha uma opção: '))
    

