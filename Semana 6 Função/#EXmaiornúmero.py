#EXmaiornúmero
def maior(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a
a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))

print("Maior valor:",maior(a,b))    