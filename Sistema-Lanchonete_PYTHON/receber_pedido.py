from dados import lanches
def receber_pedidos():
    comanda = []
    while True:
        
        pedido=int(input("Qual seu Pedido: "))

        if pedido == 0:
            break
        
        if pedido in lanches:
            comanda.append(pedido)
          
        else:
            print("Codigo errado, tente Novamente!")
        feed=str(input("Quer continuar? S/N " )).strip().upper()
        if feed == "N" or feed == "NÃO":
            break
    return comanda