#EXmaiornumerodalista

lista = [1,10,5,7,3,4,2,6,8,9]
tamanho = len(lista)
maior = lista[0]

for i in range(tamanho):
    if lista[i] >= maior:
        maior = lista[i]

print(maior)