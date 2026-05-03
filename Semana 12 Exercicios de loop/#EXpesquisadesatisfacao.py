#EXpesquisadesatisfacao

nota = True
quant = 0
media = 0
positivas = 0
neutras = 0
negativas = 0

while nota != 0:
    nota = int(input("De uma nota de 1 a 5: "))
    if nota != 0:
        quant += 1
        media += nota
        if nota >= 4:
            positivas += 1
        elif nota == 3:
            neutras += 1
        elif nota < 3:
            negativas += 1

print(f"Tiveram {quant} com a média de {media/quant} com: ")
print(f"{positivas} avaliações positivas")
print(f"{neutras} avaliações neutras")
print(f"{negativas} avaliações negativas")
