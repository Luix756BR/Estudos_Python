cont=0
numeros=[]

def lista(numeros):
    maior=max(numeros)
    menor=min(numeros)
    return maior,menor

while True:
    num=int(input("Digite um numero, caso queira parar digite (-1): "))
    cont+=1
    #numeros.append(num)
    if num == -1:
        #numeros.remove(-1)
        break
    numeros.append(num)
    
maior, menor = lista(numeros)
print(f"Numeros digitados: {numeros}")
print(f'Quantidade: {cont} numeros ')
print(f"Maior Numero: {maior} \n Menor numero {menor}")
