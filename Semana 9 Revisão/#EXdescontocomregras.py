#EXdescontocomregrascombinadas

def desconto(valor,vip):
    vip = vip.upper()
    if vip == "S":
        valor -= valor * 0.1
        return valor
    elif vip == "N":
        if valor >= 100:
            valor -= valor * 0.05
            return valor
        else:
            return valor
    else:
        print("A condição de vip tem que ser sim ou não.")

valor = float(input("Digite o valor da compra: "))
vip = input("Você é VIP?(S ou N): ")

print(f"O valor final é de {desconto(valor,vip)}")
