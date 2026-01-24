idades=[]
def rank_idade(idades):
    maior=max(idades)
    menor=min(idades)
    soma_idades=sum(idades)
    media=soma_idades/2
    return maior,menor,media

for c in range(2):
    usuario=int(input("Qual sua Idade: "))
    idades.append(usuario)

maior, menor, media = rank_idade(idades)
print(f"A maior idade: {maior}")
print(f"A menor idade é: {menor}")
print(f"A media de todas: {media}")