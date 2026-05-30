def menu():
    print("======== LANCHES =======")
    print("1 - Hamburguer: 10.00")
    print("2 - Cachorro quente: 8.00")
    print("3 - Pastel: 5.00")
    print("4 - Coxinha: 3.50")
    print("5 - Empada: 2.00")
    print("6 - X-Tudo: 15.00")

    print("======= BEBIDAS =======")
    print("7 - Água: 1.50")
    print("8 - Coca cola: 2.50")
    print("9 - Suco: 3.00")
    print("0 - Sair")


# Dicionário de produtos
produtos = {
    1: ("Hamburguer", 10.00),
    2: ("Cachorro quente", 8.00),
    3: ("Pastel", 5.00),
    4: ("Coxinha", 3.50),
    5: ("Empada", 2.00),
    6: ("X-Tudo", 15.00),
    7: ("Água", 1.50),
    8: ("Coca cola", 2.50),
    9: ("Suco", 3.00)
}

comanda = []
total = 0

while True:
    menu()
    pedido = int(input("OPA! O que deseja? "))

    if pedido == 0:
        break

    if pedido in produtos:
        nome, preco = produtos[pedido]
        comanda.append(pedido)
        total += preco
        print(f"{nome} adicionado à comanda!")
    else:
        print("Opção inválida, tente novamente.")

    continuar = input("Deseja pedir mais alguma coisa? (S/N): ").strip().upper()
    if continuar != "S" and continuar != "SIM":
        break

with open("comanda.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("======= COMANDA =======\n")
    print("\n======= COMANDA =======")
    for item in comanda:
        nome, preco = produtos[item]
        print(f"{nome} - R$ {preco:.2f}")


    arquivo.write("------------------------\n")
    arquivo.write(f"{nome} - R$ {preco:.2f}\n")
    arquivo.write(f"Total: R$ {total:.2f}\n")


print("\nPedido finalizado!")
print("A comanda foi salva no arquivo 'comanda.txt'")