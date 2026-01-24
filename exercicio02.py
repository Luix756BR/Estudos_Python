cont=0
soma=0
acumulador=0
while True:
    cont=int(input("Digite um Numero, caso queira parar Digite 0(zero): "))

    if cont==0:
        break

    soma+=cont
    acumulador+=1
    
print(f"Soma: {soma}")
print(f"Acumulador de Processos: {acumulador}")