def menu():
    print("1 - Somar")
    print("2 - subtrair")
    print("3 - Sair")

while True:
    menu()
    escolha=int(input("Qual sua escolha: "))
    if escolha == 1:
        n1=int(input("Digite um numero: "))
        n2=int(input("Digite outro numero: "))
        soma=n1+n2
        print(f"resultado: {soma}")
    elif escolha == 2:
        n1=int(input("Digite um numero: "))
        n2=int(input("Digite outro numero: "))
        sub=n1-n2
        print(f"Resultado: {sub}")
    elif escolha == 3:
        break
    else:
        print("Escolha errada, Tente Novamente!")
print("Obrigado Por participar") 


