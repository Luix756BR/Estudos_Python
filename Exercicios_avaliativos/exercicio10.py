nomes=[]
cont=0
while cont < 5:
    aluno=str(input("Digite o Nome dos Alunos: "))
    cont+=1
    nomes.append(aluno)
    tamanho=len(nomes)

print(f'Nomes : {nomes}')
print(f"Quantidade de Alunos : {tamanho}")