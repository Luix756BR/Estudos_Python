numeros=[]
cont=0

while cont < 5:
    num=int(input("Digite alguns Numeros: "))
    cont+=1
    numeros.append(num)
    maximo=max(numeros)
    minimo=min(numeros)
    
print(f"Numeros : {numeros}")
print(f"Maior Numero : {maximo}")
print(f"Menor Numero : {minimo}")
