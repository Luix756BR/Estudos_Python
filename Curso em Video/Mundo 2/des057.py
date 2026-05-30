sexo = input('Informe o sexo da pessoa: ').strip().upper()
while sexo not in 'MF':
    print('Sexo inválido! Por favor insira novamente')
    sexo = input('Informe o sexo da pessoa: ').strip().upper()