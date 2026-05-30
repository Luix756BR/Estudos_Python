def ranking(pessoas):
    idades = pessoas.values()
    maior = max(idades)
    menor = min(idades)
    return maior, menor


def menu():
    print("1 - Cadastrar usuário")
    print("2 - Mostrar Usuários")
    print("3 - Sair")

pessoas={}
while True:
    menu()
    escolha=int(input("Qual sua Escolha: "))
    if escolha == 1: 
        nome=str(input("Digite um nome: "))
        idade=int(input("Digite a Idade: "))
        pessoas[nome]=idade
        
    elif escolha == 2:
        print(pessoas)
        maior,menor = ranking(pessoas)
        print(f"A maior idade foi: {maior}")
        print(f"A Menor idade Foi: {menor}")
    elif escolha == 3:
        break
    else:
        print("Opção Errada, Tente Novamente!")
print(pessoas)
