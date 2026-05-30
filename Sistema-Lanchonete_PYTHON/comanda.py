import dados
import receber_pedido
def salvar_comanda(comanda, lanhes):
    with open("comanda.txt", "w", encoding="utf-8") as arquivo:
        total = 0

        for item in comanda:
            nome, preco = lanhes[item]
            arquivo.write(f"{nome} - R$ {preco:.2f}\n")
            total += preco

        arquivo.write(f"\nTotal: R$ {total:.2f}")
