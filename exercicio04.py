cont=0
idades=[]

def idade(idades):
    maior = max(idades)
    menor = min(idades)
    return maior,menor

while cont<2:
    idades_usuario=int(input("Qual sua idade? "))
    cont+=1
    idades.append(idades_usuario)

maior, menor = idade(idades)

print(idades)
print(f"Maior idade: {maior}")
print(f"Menor idade: {menor}")

