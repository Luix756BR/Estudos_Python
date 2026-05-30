v = float(input('Informe o valor da casa: R$'))
s = float(input('Informe o valor do salário do comprador: R$'))
a = float(input('Informe em quantos anos a casa será paga: '))
p = v/(a*12)
if p <= (0.3*s):
    print(f'O seu empréstimo de R${p:.2f} mensais foi aprovado ')
else:
    print(f'O seu empréstimo de R${p:.2f} mensais foi negado por exceder 30% do seu salário')
