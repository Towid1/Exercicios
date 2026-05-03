#EXcalculadoracomfuncoes

def soma(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a / b

def calculadora():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    tipo = input("Digite a operação desejada(+,-,*,/): ")
    if tipo == "+":
        return print(soma(a,b))
    elif tipo == "-":
        return print(subtracao(a,b))
    elif tipo == "*":
        return print(multiplicacao(a,b))
    elif tipo == "/":
        return print(divisao(a,b))
    else:
        return print("Operação inválida, tente novamente.")

calculadora()