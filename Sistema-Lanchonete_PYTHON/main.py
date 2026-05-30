from menu import menu
from receber_pedido import receber_pedidos
from dados import lanches
from comanda import salvar_comanda

menu()
comanda = receber_pedidos()

total = 0

for item in comanda:
    nome, preco = lanches[item]
    print(f"{nome} - R$ {preco:.2f}")
    total += preco

print(f"Total: R$ {total:.2f}")

salvar_comanda(comanda, lanches)
print("Comanda salva com sucesso!")

