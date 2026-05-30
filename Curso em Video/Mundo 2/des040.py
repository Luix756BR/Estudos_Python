n1 = float(input('Informe a 1° nota do aluno: '))
n2 = float(input('Informe a 2° nota do aluno: '))
m = (n1 + n2)/2
print(f'A média desse aluno foi {m:.1f} e portanto ele ', end = '')
if m < 5:
    print('foi REPROVADO')
elif m >= 5  and m <=6.9:
    print('ficou de RECUPERAÇÃO')
elif m >= 7:
    print('foi APROVADO')
