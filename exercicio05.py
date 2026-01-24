numeros=[]
def total(numeros):
    soma = sum(numeros)
    return(soma)

while True:
    num=int(input("Digite um Numero: "))
    numeros.append(num)
    feed=str(input("Quer continuar? ")).upper()
    if feed == "S" or feed=="SIM":
        print('ok')
    else:
        break

soma=total(numeros)
print(f"O total dos numeros da lista é: {soma}")

