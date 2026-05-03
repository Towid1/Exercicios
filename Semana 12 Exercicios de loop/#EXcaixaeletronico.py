#EXcaixaeletronico

saldo = float(input("Digite seu saldo atual: "))

while saldo > 0:
    saque = float(input("Digite o valor do saque: "))
    if saque <= saldo:
        saldo -= saque
        print(f"Seu saldo é de {saldo} reais")
    else:
        print("O valor de saque é maior que o saldo.")
        print(f"Saldo: {saldo}")
if saldo <= 0:
    print("Programa encerrado")