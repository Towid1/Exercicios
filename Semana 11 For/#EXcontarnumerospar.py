#contarnumerospar

lista = [1,2,3,4,5,6]
tamanho = len(lista)
pares = 0

for i in range(tamanho):
    if lista[i] % 2 == False:
        pares += 1

print(pares)