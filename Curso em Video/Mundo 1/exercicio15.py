dias= 60 #valor por diaria do aluguel
km = 0.15 #taxa pelo Quilometro rodado
var=int(input("Quantos dias você utilizou o carro: "))
var2=float(input("Quantos KM percorreu: "))

total=(var*dias) + (var2 * km)

print("Opa que coisa Boa ter você aqui, ai está sua nota fiscal pelo o aluguel do carro!")
print(f"Dias rodados: {var}")
print(f"Quilometros rodados: {var2}")
print(f"Total a pagar: {total}")