nomes=[]
while True:
    aluno=str(input("Digite o nome do aluno: ")).strip()
    nomes.append(aluno)
    nomes.sort()
    feed=str(input("Quer continuar: ")).upper().strip()
    if feed == "NÃO" or feed == "N":
        break


palavra=str(input("Escreva a palavra que Procura: "))
if palavra in nomes:
    print("Está sim")
else:
    print("Não esta")
print(nomes)