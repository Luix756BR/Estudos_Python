p = float(input('Informe o preço normal do produto: R$'))
c = input('''Informe a condição de pagamento:
[1] Á vista dinheiro/cheque: 10% de desconto
[2] Á vista no cartão: 5% de desconto
[3] Em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros\n''')
if c == '1':
    print(f'Você pagará um total de R${p*0.9:.2f}')
elif c == '2':
    print(f'Você pagará um total de R${p*0.95:.2f}')
elif c == '3':
    print(f'Você pagará 2 parcelas de R${p/2:.2f} sem juros')
    print(f'Você pagará um total de R${p:.2f}')
elif c == '4':
    par = int(input('Em quantas parcelas você quer pagar? '))
    while par <=2:
        print('Por favor insira um parcelamento válido')
        par = int(input('Em quantas parcelas você quer pagar? '))
    print(f'Você pagará {par} parcelas de R${((p*1.2)/par):.2f} com juros')
    print(f'Você pagará um total de R${p*1.2:.2f}')
else:
    print('Você não escolheu nenhuma condição de pagamento')